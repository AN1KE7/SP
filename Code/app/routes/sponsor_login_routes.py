from flask import Blueprint , render_template, request , flash , redirect , url_for
from flask_login import login_user , current_user
from werkzeug.security import check_password_hash
from app.models import User


sponsor_login = Blueprint('sponsor_login' , __name__ , template_folder='templates')

@sponsor_login.route('/sponsor_login' , methods=['GET' , 'POST'])
def sponsor_login_page():
    if request.method=='POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username , role='Sponsor').first()
        if user:
            if check_password_hash(user.password , password):
                flash('Welcome , Mighty Sponsor !' , category='success')
                login_user(user , remember='True')
                return redirect(url_for('home.home_page'))
            else:
                flash('Incorrect password , try again.' , category='error')
        else:
            flash('Sponsor does not exist.' , category='error')
    return render_template('sponsor_login.html' , user=current_user)
