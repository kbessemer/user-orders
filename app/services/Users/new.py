from ...database import db
from ...models.user import User

def new(first_name, last_name):
    new_user = User(first_name=first_name, last_name=last_name)
    
    db.session.add(new_user)
    try:
        db.session.commit()
        return new_user
    except Exception as e:
        db.session.rollback()
        return None