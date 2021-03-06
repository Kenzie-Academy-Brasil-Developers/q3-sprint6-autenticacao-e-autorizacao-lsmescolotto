from http import HTTPStatus
from flask import current_app, request, jsonify
from psycopg2 import IntegrityError
from app.models.user_model import UserModel
from app.configs.database import db
from sqlalchemy.exc import NoResultFound
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required


def register_user():
    try:
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
    except IntegrityError:
        return {"message": "Email already exists"}

def login():
    try:
        data = request.get_json()
        
        found_user = UserModel.query.filter_by(email=data["email"]).one()

        if not found_user.verify_password(data["password"]):
            return {"message": "Unauthorized"}, HTTPStatus.UNAUTHORIZED

        access_token = create_access_token(found_user)

        return {"access_token": access_token}, HTTPStatus.OK
    
    except NoResultFound:
        return {"message": "user not found"}, HTTPStatus.NOT_FOUND
    
    except:
        return {"message": "Unauthorized"}, HTTPStatus.UNAUTHORIZED



@jwt_required()
def update_user():
    try:
        data = request.get_json()

        user_to_update = get_jwt_identity()

        user = UserModel.query.filter_by(email=user_to_update["email"]).one()

        for key, value in data.items():
            setattr(user, key, value)

        db.session.add(user)
        db.session.commit()

        return jsonify(
        {"name": user.name, 
        "last_name": user.last_name, 
        "email": user.email}
        ), HTTPStatus.OK
        
    except NoResultFound:
        return {"message": "user not found"}, HTTPStatus.NOT_FOUND
    
    except:
        return {"message": "Unauthorized"}, HTTPStatus.UNAUTHORIZED


@jwt_required()
def delete_user():
    try:
        user = get_jwt_identity()
        user_to_delete = UserModel.query.filter_by(email=user["email"]).one()

        current_app.db.session.delete(user_to_delete)
        current_app.db.session.commit()

        return "", HTTPStatus.NO_CONTENT
    
    except NoResultFound:
        return {"message": "user not found"}, HTTPStatus.NOT_FOUND
    
    except:
        return {"message": "Unauthorized"}, HTTPStatus.UNAUTHORIZED

@jwt_required()
def get_users():
    try:
        user_to_get = get_jwt_identity()
        
        return jsonify(
        {"name": user_to_get["name"], 
        "last_name": user_to_get["last_name"], 
        "email": user_to_get["email"]}
        ), HTTPStatus.OK

    except NoResultFound:
        return {"message": "user not found"}, HTTPStatus.NOT_FOUND
    
    except:
        return {"message": "Unauthorized"}, HTTPStatus.UNAUTHORIZED