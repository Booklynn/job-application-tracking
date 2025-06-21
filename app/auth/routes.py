from flask import Blueprint, redirect, render_template, request, session, url_for
from app.auth.models import User
from app.extensions import db
from . import auth_bp

login_bp = Blueprint('login', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            session['user_id'] = user.id
            session['username'] = user.username
            return redirect(url_for('main.index'))
        else:
            error = 'Invalid email or password'
            return render_template('auth/login.html', error=error)
    
    return render_template('auth/login.html')

@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if 'user_id' in session:
        return redirect(url_for('main.index'))
    
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm-password')

        if User.query.filter_by(email=email).first():
            error = 'This email is already registered.'
            return render_template('auth/register.html', error=error)
        
        if password != confirm_password:
            error = 'Passwords do not match.'
            return render_template('auth/register.html', error=error)

        new_user = User(email=email, username=username, role="User")
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('auth.login'))

    return render_template('auth/register.html')