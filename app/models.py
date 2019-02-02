from app import db

class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), index=True)
    address = db.Column(db.String(120), index=True)
    city = db.Column(db.String(120), index=True)
    state = db.Column(db.String(120), index=True)
    zipcode = db.Column(db.String(120), index=True)

    def __repr__(self):
        return '<Address {}>'.format(self.name)    