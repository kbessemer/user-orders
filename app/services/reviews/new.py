from ...models.review import Review
from ...database import db


def new(item, data):
    review = Review(item=item, comment=data["comment"])
    
    db.session.add(review)
    try:
        db.session.commit()
        return review
    except Exception as e:
        db.session.rollback()
        return None