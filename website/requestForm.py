from flask import Blueprint,flash, Flask, request, render_template
from .pricingModuleSWD import *
from .client import Client, profiles
from flask_login import login_user, login_required, logout_user, current_user

#placeholder for the users state address
userstate = "TX"

requestForm = Blueprint('requestForm', __name__)

@requestForm.route('/quote-form', methods=['GET", "POST'])
def quoteFormSubmission():
    if request.method == 'POST':
        galReq = request.form.get('requestedGallons')

        if galReq is None:
            flash('Must specify number of gallons', category='error')
        elif not galReq.isdigit():
            flash('Gallons requested must be a number greater than zero', category='error')

        currentForm = PricingModule(userstate, galReq)

        suggestedPrice = currentForm.getSuggestedPPG()
        totalAmountDue = currentForm.getTotalAmtDue()

    return render_template("quote-form.html", suggestedPrice, totalAmountDue=totalAmountDue)