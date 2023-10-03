from extensions import db
class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    photo_url = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(255), nullable=False)
    offer_of_the_month = db.Column(db.Boolean, default=True)
    available = db.Column(db.Boolean, default=True)
    self_pickup = db.Column(db.Boolean, default=True)
    description = db.Column(db.String, nullable=True)
    price = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return "<User " + self.Product.name +self.Product.photo_url + ">"