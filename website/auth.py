from flask import Blueprint, render_template, request, flash, redirect, url_for
from .client import Client, profiles
from datetime import datetime

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get data from front end
        username = request.form.get('username')
        password = request.form.get('password')

        for client in profiles:
            if client.username == username and client.password == password:
                curr_client = client
                profiles.remove(client)
                profiles.append(curr_client)
                
                if client.logintime == None:
                    #first time user detected
                    logintime = datetime.now()
                    client.logintime = logintime
                    flash('Logged in successfully! Please create your profile.', category='success')
                    return render_template("profile.html", userauthentic = True)

                    #take other clients to home page
                logintime = datetime.now()
                client.logintime = logintime
                flash('Logged in successfully!', category='success')
                return render_template("home.html", userauthentic = True)
                
               
        flash('Credentials are incorrect. Please try again.', category='error')
    return render_template("login.html", userauthentic = False)
    

@auth.route('/logout')
def logout():
    return redirect(url_for('auth.login',userauthentic = False))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        # Get info from front end. Will eventually persist through DB
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        exists = None
        for client in profiles:
            if client.username == username:
                exists = True

        if exists:
            flash('Username already exists. Please try again', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match. Please try again', category='error')
        else:
            new_client = Client(username=username, password=password1, logintime = None)
            profiles.append(new_client) #persist through db
            #direct clients to log in for the first time
            flash('Account created successfully! Please Log in.', category='success')
            return redirect(url_for('auth.login',userauthentic = False))


            
    return render_template("sign_up.html", user=current_user)

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

