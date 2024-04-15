from ...models.order import Order
from ...models.item import Item
from ...database import db

def post(user, item_ids):
    order = Order(user=user)

    for item_id in item_ids:
        item = Item.query.get(item_id)
        if item:
            order.items.append(item)
    
    db.session.add(order)
    try:
        db.session.commit()
        return order
    except Exception as e:
        db.session.rollback()
        return None