from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .client import Client, profiles
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])

def home():
    return render_template("home.html",  userauthentic = True)


@views.route('/quote-form')
def form():
    return render_template("quote-form.html",  userauthentic = True)

@views.route('/quote-history')
def history():
    return render_template("quote-history.html",  userauthentic = True)

@views.route('/get-quote-history', methods=['GET', 'POST'])
def get_fuel_quote_history():
    fuel_quote_history = [
        {'date': '2022-03-15', 'gallons': 100,'address': '4401 Cougar Village Drive','delivery_date': '2022-04-04', 'msrp': 258.67, 'total_price': 250.00},
        {'date': '2022-02-22', 'gallons': 75,'address': '3875 Holman Street', 'delivery_date': '2022-03-6', 'msrp': 190.00, 'total_price': 187.50},
        {'date': '2022-01-28', 'gallons': 50,'address': '4300 University Drive','delivery_date': '2022-03-07', 'msrp': 126.50, 'total_price': 125.00}
    ]
    return render_template("quote-history.html", fuel_quote_history=fuel_quote_history,  userauthentic = True)
