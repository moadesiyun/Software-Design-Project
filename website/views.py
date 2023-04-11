from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from . import db
from .dbmodels import userCredentials, Profile
from flask_login import login_user, login_required, logout_user, current_user
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    return render_template("home.html", user=current_user)


@views.route('/display', methods=['GET', 'POST'])
@login_required
def display():
    return render_template("display.html", user=current_user)

@views.route('/quote-history')
@login_required
def history():
    return render_template("quote-history.html",user=current_user)

@views.route('/get-quote-history', methods=['GET', 'POST'])
@login_required
def get_fuel_quote_history():
    CurrentUser = userCredentials.query.filter_by(id=current_user.id).first()
    
    fuelquotes = CurrentUser.fuelquotes
    return render_template("quote-history.html", fuel_quote_history=fuelquotes, user=current_user)
