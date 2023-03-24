from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db   ##means from __init__.py import db
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)

client_profiles = []

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get data from front end
        username = request.form.get('username')
        password = request.form.get('password')

        #hardcoded user and pass for now
        if username == "jurnae" and password == "jones":
            flash('Logged in successfully!', category='success')
            return render_template("home.html", user=current_user)
            # take to profile page if first time user (login time is not null/None). Get from DB.

        flash('Credentials are incorrect. Please try again.', category='error')
        return render_template("login.html", user=current_user)

    #otherwise, return to login lage
    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        # Get info from front end. Will eventually persist through DB
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        if username =="jurnae":
            flash('Username already exists. Please try again.', category='error')

        elif password1 != password2:
            flash('Passwords don\'t match. Please try again.', category='error')

        else:
            flash('Account created successfully!', category='success')
            ''' persist user and pass through the DB here and take back to login page
             it will go straight to profile page for now '''
            return render_template("profile.html", user=current_user)

    return render_template("sign_up.html", user=current_user)

@auth.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if request.method == 'POST':
        fName = request.form.get('fname')
        lName = request.form.get('lname')
        userAdd1 = request.form.get('userAddress1')
        userAdd2 = request.form.get('userAddress2')
        uCity = request.form.get('city')
        st = request.form.get('state')
        zipcd = request.form.get('zipcode')
        if len(uCity) < 5:
            flash('Passwords don\'t match.', category='error')
        elif len(zipcd) < 5:
            flash('Zipcode must be at least 7 characters.', category='error')
        else:
            updated_profile = Profile(fname=fName, lname =lName, userAddress1 =userAdd1, userAddress2 =userAdd2, city=uCity, state=st, zipcode=zipcd, user_id=current_user.id)  #providing the schema for the note 
            db.session.add(updated_profile) #adding the note to the database 
            db.session.commit()
            flash('Profile information updated!', category='success')
            
    return render_template("profile.html", user=current_user)


