from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import AddressForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    return render_template('index.html', title='Home', user=user)
@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AddressForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('add.html',  title='Sign In', form=form)