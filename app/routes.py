from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import AddressForm
from app.models import Addresses
from flask import request
from flask import jsonify

@app.route('/')
@app.route('/addresses/all')
def index():
    allAddresses = Addresses.query.all()
    for address in allAddresses:
      print(address.name)
      print(address.address)
      print(address.city)
      print(address.state)
      print(address.zipcode)
    return 'test'

@app.route('/addresses/add', methods=['GET', 'POST'])
def add():
    data = request.get_json()
    address = Addresses(name=data['name'], address=data['address'], city=data['city'], state=data['state'], zipcode=data['zipcode'])
    db.session.add(address)
    db.session.commit()
    return address

@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
  Addresses.query.filter_by(id=id).delete()
  db.session.commit()
  return redirect(url_for('index'))
