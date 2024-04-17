from ...models.item import Item
from sqlalchemy.orm import joinedload

def lookup(id):
    item = Item.query.options(
            joinedload(Item.reviews)
        ).filter_by(id=id).first()
    
    if item:
        return item
    else:
        return None