from http import HTTPStatus
from flask import current_app, request, jsonify
from app.models.user_model import UserModel, auth
from app.configs.database import db
from sqlalchemy.exc import NoResultFound


def register_user():
    data = request.get_json()

    password_to_hash = data.pop("password")

    new_user = UserModel(**data)
    new_user.password = password_to_hash
    print(new_user)

    db.session.add(new_user)
    db.session.commit()

    return jsonify(
        {"name": new_user.name, 
        "last_name": new_user.last_name, 
        "email": new_user.email}
        ), HTTPStatus.CREATED


def login():
    try:
        data = request.get_json()
        
        found_user = UserModel.query.filter_by(email=data["email"]).one()
        print(found_user)
        if not found_user.verify_password(data["password"]):
            return {"message": "Unauthorized"}, HTTPStatus.UNAUTHORIZED

        return {"api_key": found_user.api_key}, HTTPStatus.OK
    
    except NoResultFound:
        return {"message": "user not found"}, HTTPStatus.NOT_FOUND
    
    except:
        return {"message": "Unauthorized"}, HTTPStatus.UNAUTHORIZED



@auth.login_required
def update_user():
    try:
        data = request.get_json()

        print(auth.current_user())

        user_to_update = auth.current_user()

        for key, value in data.items():
            setattr(user_to_update, key, value)

        db.session.add(user_to_update)
        db.session.commit()

        return jsonify(
        {"name": user_to_update.name, 
        "last_name": user_to_update.last_name, 
        "email": user_to_update.email}
        ), HTTPStatus.OK
        
    except NoResultFound:
        return {"message": "user not found"}, HTTPStatus.NOT_FOUND
    
    except:
        return {"message": "Unauthorized"}, HTTPStatus.UNAUTHORIZED


@auth.login_required
def delete_user():
    try:
        user_to_delete = auth.current_user()

        current_app.db.session.delete(user_to_delete)
        current_app.db.session.commit()

        return "", HTTPStatus.NO_CONTENT
    
    except NoResultFound:
        return {"message": "user not found"}, HTTPStatus.NOT_FOUND
    
    except:
        return {"message": "Unauthorized"}, HTTPStatus.UNAUTHORIZED

@auth.login_required
def get_users():
    try:
        user_to_get = auth.current_user()
        print(auth.current_user())
        return jsonify(
        {"name": user_to_get.name, 
        "last_name": user_to_get.last_name, 
        "email": user_to_get.email}
        ), HTTPStatus.OK

    except NoResultFound:
        return {"message": "user not found"}, HTTPStatus.NOT_FOUND
    
    except:
        return {"message": "Unauthorized"}, HTTPStatus.UNAUTHORIZED