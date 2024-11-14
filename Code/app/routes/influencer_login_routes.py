from flask import Blueprint , render_template , request , flash , redirect , url_for
from app.models import User
from werkzeug.security import check_password_hash 
from flask_login import current_user , login_user

influencer_login = Blueprint('influencer_login' , __name__ , template_folder='templates')

@influencer_login.route('/influencer_login' , methods=['GET','POST'] )
def influencer_login_page():
    if request.method=='POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username , role='Influencer').first()
        if user:
            if check_password_hash(user.password , password):
                flash('Welcome , Awesome Influencer !' , category='success')
                login_user(user , remember='True')
                return redirect(url_for('home.home_page'))
            else:
                flash('Incorrect password , try again.' , category='error')
        else:
            flash('Influencer does not exist.' , category='error')

    return render_template('influencer_login.html' , user=current_user)