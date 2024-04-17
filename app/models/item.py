from ..database import db

class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100))
    price = db.Column(db.Float, nullable=False)
    reviews = db.relationship('Review', backref='item')
    orders = db.relationship('OrderItem', back_populates='item')