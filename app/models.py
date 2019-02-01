from app import db

class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), index=True, unique=True)
    address = db.Column(db.String(120), index=True, unique=True)
    city = db.Column(db.String(120), index=True, unique=True)
    state = db.Column(db.String(120), index=True, unique=True)
    zipcode = db.Column(db.String(120), index=True, unique=True)

    def __repr__(self):
        return '<Address {}>'.format(self.name)    