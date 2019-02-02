from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import AddressForm
from app.models import Addresses
from pyusps import address_information

@app.route('/')
@app.route('/index')
def index():
    addresses = Addresses.query.all()
    return render_template('index.html', title='Home', addresses=addresses)
@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AddressForm()
    if form.validate_on_submit():
      addr = dict([
      ('address', form.address.data),
      ('city', form.city.data),
      ('state', form.state.data),
      ('zipcode', form.zipcode.data)
      ])

      try:
        address_information.verify('081NA0000050', addr)
        print("good address")
        address = Addresses(name=form.name.data, address=form.address.data, city=form.city.data, state=form.state.data, zipcode=form.zipcode.data)
        db.session.add(address)
        db.session.commit()
        flash('Address added for {}'.format(form.name.data))
        return redirect(url_for('index'))
      except Exception as e:
        print(e)
        return render_template('add.html',  title='Sign In', form=form, message="Address is incorrect")
    return render_template('add.html',  title='Sign In', form=form)
@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
  Addresses.query.filter_by(id=id).delete()
  db.session.commit()
  return redirect(url_for('index'))
