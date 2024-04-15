from ...models.item import Item

def get(id):
    item = Item.query.filter_by(id=id).first()

    if item:
        return item
    else:
        return None