from ...models.order import Order
from sqlalchemy.orm import joinedload

def lookup(id):
    order = Order.query.options(joinedload(Order.items)).filter_by(id=id).first()

    if order:
        return order
    else:
        return None
