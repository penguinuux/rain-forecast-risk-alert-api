from http import HTTPStatus

from app.configs.database import db
from app.models.user_model import UserModel
from flask import jsonify, request, session
from flask_jwt_extended import (create_access_token, get_jwt_identity,
                                jwt_required)
from sqlalchemy.orm import Session


def signup():
    ...


def signin():
    data = request.get_json()

    user:UserModel = (UserModel.query.filter_by(email=data['email']).first())

    if not user:
        return {'message':'User not found'},HTTPStatus.NOT_FOUND
    
    if user.verify_password(data['password']):
        token = create_access_token(user)
        return {'token': token},HTTPStatus.OK

    else:
        return {'message':'Unauthorized'},HTTPStatus.UNAUTHORIZED

@jwt_required()
def get_user():
    ...

@jwt_required()
def delete_user():
    ...

@jwt_required()
def patch_user():
    ...