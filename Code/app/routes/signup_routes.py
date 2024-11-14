from flask import Blueprint , render_template , request , flash , redirect , url_for
from app.models import User
from werkzeug.security import generate_password_hash 
from app import db
from flask_login import current_user
from sqlalchemy.exc import IntegrityError


signup = Blueprint('signup' , __name__ , template_folder='templates')

@signup.route('/sign-up' ,  methods=['GET','POST'] )
def signup_page():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        role = request.form.get('role')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        user = User.query.filter_by(username=username , role=role).first()
        email_exists = User.query.filter_by(email=email).first()

        if user:
            flash('Username already exists. Please choose another email.', category='error')
        elif email_exists:
            flash('Email already registered. Please use another email or login.', category='error')
        elif len(username)<3:
            flash('Username must contain atleast 3 characters.' , category='error')
            pass
        elif len(password)<6:
            flash('Password must be atleast 6 characters.' , category='error')
            pass
        elif password != confirm_password:
            flash('Passwords do not match.' , category='error')
            pass 
        else:
            try:
                #add user to database
                new_user =   User(username=username , email=email , role=role , password=generate_password_hash(password , method="scrypt" , salt_length=16))
                db.session.add(new_user)
                db.session.commit()
                flash('Account created !' , category='success')
                return redirect (url_for('home.home_page'))
            except IntegrityError :
                db.session.rollback()  # Rollback the session to avoid issues with the current transaction
                flash('Username is already taken for the role .', category='error')



    return render_template('signup.html' , user=current_user)