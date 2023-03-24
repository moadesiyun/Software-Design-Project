from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Profile
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    return render_template("home.html", user=current_user)


@views.route('/quote-form')
@login_required
def form():
    return render_template("quote-form.html", user=current_user)

@views.route('/quote-history')
@login_required
def history():
    return render_template("quote-history.html", user=current_user)

@views.route('/get-quote-history', methods=['GET', 'POST'])
@login_required
def get_fuel_quote_history():
    fuel_quote_history = [
        {'date': '2022-03-15', 'gallons': 100,'address': '4401 Cougar Village Drive','delivery_date': '2022-04-04', 'msrp': 258.67, 'total_price': 250.00},
        {'date': '2022-02-22', 'gallons': 75,'address': '3875 Holman Street', 'delivery_date': '2022-03-6', 'msrp': 190.00, 'total_price': 187.50},
        {'date': '2022-01-28', 'gallons': 50,'address': '4300 University Drive','delivery_date': '2022-03-07', 'msrp': 126.50, 'total_price': 125.00}
    ]
    return render_template("quote-history.html", fuel_quote_history=fuel_quote_history, user=current_user)
