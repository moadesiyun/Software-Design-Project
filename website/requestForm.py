from flask import Blueprint,flash, Flask, request, render_template
from .pricingModuleSWD import *
from .client import Client, profiles
from . import db
from .dbmodels import userCredentials, Profile
from flask_login import login_user, login_required, logout_user, current_user
import dbmodels


requestForm = Blueprint('requestForm', __name__)

@requestForm.route('/quote-form', methods=['GET", "POST'])
def quoteFormSubmission():
    if request.method == 'POST':
        currentUser = fuelQuote.query.filter_by(username=username).first()
        galReq = request.form.get('requestedGallons')

        if galReq is None:
            flash('Must specify number of gallons', category='error')
        elif not galReq.isdigit():
            flash('Gallons requested must be a number greater than zero', category='error')

        currentForm = PricingModule(currentUser.state, galReq)

        suggestedPrice = currentForm.getSuggestedPPG()
        totalAmountDue = currentForm.getTotalAmtDue()

        newQuoteForm = fuelQuote(gallonsRequested = galReq, suggestedPPG = suggestedPrice, totalAmountDue = totalAmountDue)
        db.session.add(newQuoteForm)
        db.session.commit()

    return render_template("quote-form.html", suggestedPrice, totalAmountDue=totalAmountDue)