from ...models.order import Order
from ...models.item import Item
from ...models.order_item import OrderItem
from ...database import db


def new(user, item_data):
    order = Order(user=user)

    for data in item_data:
        item_id = data["id"]
        quantity = data["quantity"]
        
        item = Item.query.get(item_id)
        if item:
            order_item = OrderItem(item=item, order=order, quantity=quantity)
            order.items.append(order_item)
    
    db.session.add(order)
    try:
        db.session.commit()
        return order
    except Exception as e:
        db.session.rollback()
        return None