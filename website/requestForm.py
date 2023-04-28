from flask import Blueprint, flash, request, render_template, redirect, url_for
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
        Curruser = userCredentials.query.filter_by(id=current_user.id).first()
        fuelquotes = Curruser.fuelquotes
        if fuelquotes is None:
            rateHistFactor = 0
        else:
            rateHistFactor = 0.01
        
        if galReq is None:
            flash('Must specify number of gallons', category='error')
        
        try:
            galReq = int(galReq)
        except:
            flash('Gallons requested must be a number greater than zero', category='error')
        if(currUser.address1 is None):
            flash('Must have address present in profile', category='error')
        
        
        currentForm = PricingModule(currentUser.state, galReq, rateHistFactor)

        suggestedPrice = currentForm.getSuggestedPPG()
        totalAmtDue = currentForm.getTotalAmtDue()
        if request.form.get('action2') == 'Submit':
            newQuoteForm = fuelQuote(gallons = galReq, sugppg = suggestedPrice,date = date.today(),delivery_date =deliverydate,address= currentUser.address1,  totaldue = totalAmtDue, user_id=current_user.id)
            db.session.add(newQuoteForm)
            db.session.commit()
            msg = 'Quote Saved!'
            msg2 = ' Your total calculated for '+ str(galReq) + ' gallons is: '+ str(totalAmtDue) 
            flash(msg, category='success')
            flash(msg2, category='success')
        if request.form.get('action1') == 'Get Quote':
            msg = 'Quote Generated!'
            flash(msg, category='success')
            return render_template("quote-form.html",user=current_user, total = totalAmtDue, sugg=suggestedPrice, gallons =galReq)
        

    return render_template("quote-form.html",user=current_user)