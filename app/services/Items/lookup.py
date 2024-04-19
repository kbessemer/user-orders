from ...models.item import Item
from sqlalchemy import select, func
from sqlalchemy.orm import attributes
from ...database import db

def lookup(id, page, pageSize):
    item = db.session.query(Item).filter_by(id=id).first()
    
    if item is None:
        return None
    
    item_state = attributes.instance_state(item)

    offset = (page - 1) * pageSize

    total_reviews_count = db.session.query(func.count()).select_from(Item.reviews.property.mapper.class_).filter_by(item_id=id).scalar()
    total_pages = (total_reviews_count + pageSize - 1) // pageSize

    reviews_query = select(Item.reviews.property.mapper.class_) \
        .where(Item.reviews.property.mapper.class_.item_id == id) \
        .limit(pageSize) \
        .offset(offset)
    item.reviews = db.session.execute(reviews_query).scalars().all()

    return {
        "item": item,
        "pagination": {
            "currentPage": page,
            "pageSize": pageSize,
            "totalReviews": total_reviews_count,
            "totalPages": total_pages
        }
    }
