from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db 
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from .client import Client, profiles
from datetime import datetime

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get data from front end
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(uname=username).first()
        if user:
            if check_password_hash(user.password, password):
                login_user(user, remember=True)

        for client in profiles:
            if client.username == username and client.password == password:
                if client.logintime == None:
                    #first time user detected
                    logintime = datetime.now()
                    client.logintime = logintime
                    flash('Logged in successfully! Please create your profile.', category='success')
                    return render_template("profile.html", user=current_user)

                    #take other clients to home page
                logintime = datetime.now()
                client.logintime = logintime
                flash('Logged in successfully!', category='success')
                return render_template("home.html", user=current_user)
                
               
        flash('Credentials are incorrect. Please try again.', category='error')
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
        
        user = User.query.filter_by(uname=username).first()
        if user:
            flash('Email already exists.', category='error')
        else:
            for client in profiles:
                if client.username == username:
                    ##flash('Username already exists. Please try again', category='error')
                    return render_template("sign_up.html", user=current_user)

            if password1 != password2:
                flash('Passwords don\'t match. Please try again', category='error')
            else:
                new_user = User(uname=username, password=generate_password_hash(
                    password1, method='sha256'))
                db.session.add(new_user)
                db.session.commit()
                new_client = Client(username=username, password=password1, logintime = None)
                profiles.append(new_client) #persist through db
                #direct clients to log in for the first time
                flash('Account created successfully! Please Log in.', category='success')
                return redirect(url_for('auth.login'))


            
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
        
        for client in profiles:
            if client.username == current_user.uname:
                client.update_profile_info(fName, lName, userAdd1, userAdd2, uCity, st, zipcd)
                flash('Profile information updated!', category='success')
            
    return render_template("profile.html", user=current_user)


