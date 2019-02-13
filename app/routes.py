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
    allAddressesList = []
    for address in allAddresses:
      newAddress = {
        'id': address.id,
        'name': address.name,
        'address': address.address,
        'city': address.city,
        'state': address.state,
        'zipcode': address.zipcode
      }
      allAddressesList.append(newAddress)
    return jsonify(allAddressesList)

@app.route('/addresses/add', methods=['POST'])
def add():
    data = request.get_json()
    address = Addresses(name=data['name'], address=data['address'], city=data['city'], state=data['state'], zipcode=data['zipcode'])
    db.session.add(address)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/addresses/delete/<int:id>', methods=['GET', 'POST', 'DELETE'])
def delete(id):
  Addresses.query.filter_by(id=id).delete()
  db.session.commit()
  return 'deleted address'
