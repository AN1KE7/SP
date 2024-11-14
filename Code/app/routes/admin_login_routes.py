from flask import Blueprint , render_template, request , flash , redirect , url_for
from flask_login import login_user , current_user
from werkzeug.security import check_password_hash
from app.models import User

admin_login = Blueprint('admin_login' , __name__ , template_folder='templates')

@admin_login.route('/admin_login' , methods=['GET','POST'])
def admin_login_page():
    if request.method=='POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username , role='Admin').first()
        if user:
            if check_password_hash(user.password , password):
                flash('Welcome , Worthy Admin !' , category='success')
                login_user(user , remember='True')
                return redirect(url_for('home.home_page'))
            else:
                flash('Incorrect password , try again.' , category='error')
        else:
            flash('Admin does not exist.' , category='error')
    return render_template('admin_login.html' ,  user=current_user)