from flask import render_template, redirect, url_for, flash, Blueprint
from app import db
from app.forms import RegistrationForm, LoginForm
from app.models import User
from flask_login import current_user, login_user, logout_user, login_required

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/index')
def index():
    return render_template('home.html', title='Home')

@main.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('main.login'))
    return render_template('signup.html', title='Signup', form=form)


@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid credentials', 'error')
            return render_template('login.html', title='Sign In', form=form)
        login_user(user)
        return redirect(url_for('main.dashboard'))
    return render_template('login.html', title='Sign In', form=form)

@main.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@main.route('/about_us')
def about_us():
    return render_template('about_us.html', title='AboutUs')

@main.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', title='Dashboard')
