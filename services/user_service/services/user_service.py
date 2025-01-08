from services.user_service.models.user_model import User
from services.common.config import db

def get_user(user_id):
    user = User.query.get(user_id)
    if user:
        return {"id":user.id, "name":user.name,"email":user.email}
    return None

def create_user(data):
    user = User(name=data["name"],email=data["email"])
    db.session.add(user)
    db.session.commit()
    return {"id": user.id, "name": user.name, "email": user.email}


def update_user(user_id, data):
    user = User.query.get(user_id)
    if not user:
        return None
    user.name = data.get("name", user.name)
    user.email = data.get("email", user.email)
    db.session.commit()
    return {"id": user.id, "name": user.name, "email": user.email}

def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return False
    db.session.delete(user)
    db.session.commit()
    return True