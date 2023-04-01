from flask import Blueprint, render_template, request, flash, redirect, url_for
from .client import Client, profiles
from .dbmodels import userCredentials
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get data from front end
        username = request.form.get('username')
        password = request.form.get('password')

        client = userCredentials.query.filter_by(username=username).first()

        if client:
            if check_password_hash(client.password, password):

                if client.loginTime == False:
                    client.loginTime = True
                    db.session.commit()
                    flash('Logged in successfully! Please create your profile.', category='success')
                    login_user(client, remember = True)
                    #redirect to profile page
                    return redirect(url_for('auth.profile',userauthentic = True))
                    
                else:
                    flash('Logged in successfully!', category='success')
                    login_user(client, remember = True)
                    #redirect to homepage
                    return redirect(url_for('views.home',userauthentic = True))
                   
            else:
                 flash('Incorrect password.', category='error')
        else:
            flash('Username does not exist.', category='error')

    return render_template("login.html", userauthentic = False)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login',userauthentic = False))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        # Get info from front end. Will eventually persist through DB
        username = request.form.get('username')
        password_1 = request.form.get('password1')
        password_2 = request.form.get('password2')
        
        clientCred = userCredentials.query.filter_by(username=username).first()

        if clientCred:
            flash('Username already exists.', category='error')

        elif len(username) < 5:
            flash('Username must be 5 or more characters', category='error')

        elif password_1 != password_2:
            flash('Passwords must match. Try again.', category='error')

        elif len(password_1) < 5:
            flash('Password must be 5 or more characters', category='error')

        else:
            new_client = userCredentials(username = username, password= generate_password_hash(password_1, method='sha256'), loginTime = False)
            db.session.add(new_client)
            db.session.commit()
            flash('Account created successfully! Please log in.', category='success')
            return redirect(url_for('auth.login',userauthentic = False))
            
    return render_template("sign_up.html", userauthentic = False)

@auth.route('/profile', methods=['GET', 'POST'])
def profile():
    if request.method == 'POST':
        fName = request.form.get('fname')
        lName = request.form.get('lname')
        userAdd1 = request.form.get('userAddress1')
        userAdd2 = request.form.get('userAddress2')
        uCity = request.form.get('city')
        st = request.form.get('state')
        zipcd = request.form.get('zipcode')
        
        if len(profiles)>1:
            curr_client = profiles[-1]
            curr_client.update_profile_info(fName, lName, userAdd1, userAdd2, uCity, st, zipcd)
            flash('Profile information updated!', category='success')
            
    return render_template("profile.html", userauthentic = True)

