from http import HTTPStatus
from flask import current_app, request, jsonify
from app.models.user_model import UserModel
from app.configs.database import db
from sqlalchemy.exc import NoResultFound
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity


def register_user():
    data = request.get_json()

    password_to_hash = data.pop("password")

    data = data

    new_user = UserModel(**data)
    new_user.password = password_to_hash

    db.session.add(new_user)

    db.session.add(new_user)
    db.session.commit()

    return jsonify(new_user), HTTPStatus.CREATED


def login():
    try:
        data = request.get_json()

        found_user = UserModel.query.filter_by(email=data["email"]).one()
        if not found_user.verify_password(data["password"]):
            return {"message": "Unauthorized"}, HTTPStatus.UNAUTHORIZED
        access_token = create_access_token(identity=data["email"])
        return {"access_token": f'{access_token}'}, HTTPStatus.OK
    
    except NoResultFound:
        return {"msg": "user not found"}, HTTPStatus.NOT_FOUND
        # If password doesn't match return {"message": "Unauthorized"}, HTTPStatus.UNAUTHORIZED



@jwt_required()
def update_user():
    try:
        data = request.get_json()

        user_to_update = UserModel.query.get(id)

        for key, value in data.items():
            setattr(user_to_update, key, value)

        db.session.add(user_to_update)
        db.session.commit()

        return jsonify(user_to_update), HTTPStatus.OK

    except NoResultFound:
        return {"msg": "user not found"}, HTTPStatus.NOT_FOUND
        # If password doesn't match return {"message": "Unauthorized"}, HTTPStatus.UNAUTHORIZED


@jwt_required()
def delete_user():
    pass


@jwt_required()
def get_users():
    pass