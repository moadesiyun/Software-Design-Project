from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note, Profile
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():

    return render_template("home.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():  
    note = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})

@views.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if request.method == 'POST':
        if request.method == 'POST':
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        userAdd1 = request.form.get('userAddress1')
        userAdd2 = request.form.get('userAddress2')
        uCity = request.form.get('city')
        st = request.form.get('state')
        zipcd = request.form.get('password2')
        if len(lname) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(uCity) < 5:
            flash('Passwords don\'t match.', category='error')
        elif len(zipcd) < 5:
            flash('Zipcode must be at least 7 characters.', category='error')
        else:
            updated_profile = Profile(fname=fname, lname =lname, userAddress1 =userAdd1, userAddress2 =userAdd2, city=uCity, state=st, zipcode=zipcd, user_id=current_user.id)  #providing the schema for the note 
            db.session.add(updated_profile) #adding the note to the database 
            db.session.commit()
            flash('Profile information updated!', category='success')
            
    return render_template("profile.html", user=current_user)

@views.route('/quote-form', methods=['GET', 'POST'])
@login_required
def form():
    return render_template("quote-form.html", user=current_user)

@views.route('/quote-history', methods=['GET', 'POST'])
@login_required
def history():
    return render_template("quote-history.html", user=current_user)
