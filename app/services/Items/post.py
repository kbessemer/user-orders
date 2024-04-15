from ...database import db
from ...models.item import Item

def post(product_name, product_price):
    new_item = Item(product_name=product_name, price=product_price)
    
    db.session.add(new_item)
    try:
        db.session.commit()
        return new_item
    except Exception as e:
        db.session.rollback()
        return None