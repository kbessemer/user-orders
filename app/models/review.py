from ..database import db

class Review(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(500))
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'))