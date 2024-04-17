from ...models.user import User
from ...models.order import Order
from ...models.item import Item
from ...models.review import Review
from sqlalchemy.orm import joinedload

def lookup(id):
    user = User.query.options(
        joinedload(User.orders).joinedload(Order.items)
    ).filter_by(id=id).first()

    if user:
        return user
    else:
        return None