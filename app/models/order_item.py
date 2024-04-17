from ..database import db

class OrderItem(db.Model):
    __tablename__ = 'order_items'
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'), primary_key=True)
    quantity = db.Column(db.Integer)

    order = db.relationship('Order', back_populates='items')
    item = db.relationship('Item', back_populates='orders')