from flask import Blueprint,render_template 
from flask_login import login_required , logout_user 

logout_me = Blueprint('logout' , __name__ , template_folder='templates')

@logout_me.route('/logout')
@login_required
def logoutuser():
    logout_user()
    return render_template('home.html')

