from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import AddressForm
from app.models import Address
import requests
from xml.etree import ElementTree
import xml.dom.minidom
from usps import USPSApi, Address

@app.route('/')
@app.route('/index')
def index():
    addresses = Address.query.all()
    return render_template('index.html', title='Home', addresses=addresses)
@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AddressForm()

    url = 'http://production.shippingapis.com/ShippingAPI.dll?API=ZipCodeLookup&XML=<ZipCodeLookupRequest%20USERID=081NA0000050><Address><Address1></Address1><Address2>6406 Ivy Lane</Address2><City>Greenbelt</City><State>MD</State></Address></ZipCodeLookupRequest>'

    response = requests.get(url)

    if response.status_code == 200:
      print("call went well")
      print(response)
      print(response.text)
      # tree = ElementTree.fromstring(response.content)
      # for child in tree.iter('*'):
      #   print(child.tag)
      #   print(child.attrib)


    # if tree.status_code != 200:
        # This means something went wrong.
    #     raise ApiError('GET /tasks/ {}'.format(tree.status_code))
    # for todo_item in tree.json():
    #     print(todo_item)
        # print('{} {}'.format(todo_item['id'], todo_item['summary']))
    
    # if form.validate_on_submit():
    #     address = Address(name=form.name.data, address_1=form.address.data, city=form.city.data, state=form.state.data, zipcode=form.zipcode.data)

    #     usps = USPSApi('081NA0000050', test=True)
    #     validation = usps.validate_address(address)
    #     print(validation.result)

    #     db.session.add(address)
    #     db.session.commit()
    #     flash('Address added for {}'.format(form.name.data))
    #     return redirect(url_for('index'))
    return render_template('add.html',  title='Sign In', form=form)
@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
  Address.query.filter_by(id=id).delete()
  db.session.commit()
  return redirect(url_for('index'))
