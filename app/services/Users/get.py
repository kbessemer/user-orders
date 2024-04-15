from ...models.user import User
from ...models.order import Order
from sqlalchemy.orm import joinedload, subqueryload

def get(id):
    user = User.query.options(
        subqueryload(User.orders).joinedload(Order.items)
    ).filter_by(id=id).first()

    if user:
        return user
    else:
        return None