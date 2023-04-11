from flask import Blueprint, flash, request, render_template
from flask_login import login_user, login_required, logout_user, current_user
from . import db
from .dbmodels import *
from .pricingModuleSWD import *
from datetime import date


requestForm = Blueprint('requestForm', __name__)


@requestForm.route('/quote-form')
@login_required
def form():
    return render_template("quote-form.html", user=current_user)


@requestForm.route('/get-quote-form', methods=['GET', 'POST'])
@login_required
def quote_form():
    if request.method == 'POST':
        currentUser  = Profile.query.filter_by(user_id=current_user.id).first()
        galReq = request.form.get('requestedGallons')
        deliverydate = request.form.get('deliveryDate')
        
        if galReq is None:
            flash('Must specify number of gallons', category='error')
        
        try:
            galReq = int(galReq)
        except:
            flash('Gallons requested must be a number greater than zero', category='error')
        
        
        currentForm = PricingModule(currentUser.state, galReq)

        suggestedPrice = currentForm.getSuggestedPPG()
        totalAmtDue = currentForm.getTotalAmtDue()
        
        newQuoteForm = fuelQuote(gallons = galReq, sugppg = suggestedPrice,date = date.today(),delivery_date =deliverydate,  totaldue = totalAmtDue, user_id=current_user.id)
        db.session.add(newQuoteForm)
        db.session.commit()
        flash('Quote Generated!', category='success')
        

    return render_template("quote-form.html",user=current_user)