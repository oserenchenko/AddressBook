from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import AddressForm
from app.models import Addresses
# import requests
from usps import USPSApi, Address
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
      # address = Address(name=form.name.data, address_1=form.address.data, city=form.city.data, state=form.state.data, zipcode=form.zipcode.data)

      addr = dict([
      ('address', form.address.data),
      ('city', form.city.data),
      ('state', form.state.data),
      ('zipcode', form.zipcode.data)
      ])
      try:
        address_information.verify('081NA0000050', addr)
        print("good address")
      except Exception as e:
        print(e)

      # if address_information.verify('081NA0000050', addr).startswith('ValueError'):
      #   print("The address is incorrect")




      # usps = USPSApi('081NA0000050', test=True)
      # validation = usps.validate_address(address)
      # print(validation.result)


        # db.session.add(address)
        # db.session.commit()
        # flash('Address added for {}'.format(form.name.data))
        # return redirect(url_for('index'))
    return render_template('add.html',  title='Sign In', form=form)
@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
  Addresses.query.filter_by(id=id).delete()
  db.session.commit()
  return redirect(url_for('index'))
