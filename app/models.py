from app import db

class Addresses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), index=True)
    address = db.Column(db.String(120))
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    zipcode = db.Column(db.String(5))

    def __repr__(self):
        return '<Address {}>'.format(self.name)    