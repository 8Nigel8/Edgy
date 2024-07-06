from datetime import timedelta

from flask import Blueprint, request
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity

from src.main.common import generate_response
from src.main.models.services.UserService import users_service

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


def generate_authentication_response_data(user_info):
    access_token = create_access_token(
        identity=user_info['id']
    )
    refresh_token = create_refresh_token(
        identity=user_info['id']
    )
    return {
        'access_token': access_token,
        'refresh_token': refresh_token,
        'user_info': user_info
    }


@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    user_info = users_service.create_user(data)
    response_data = generate_authentication_response_data(user_info)
    return generate_response(201, response_data)


@auth_bp.route('/login', methods=["POST"])
def login_user():
    data = request.get_json()
    user_info = users_service.login_user(data)
    response_data = generate_authentication_response_data(user_info)
    return generate_response(200, response_data)


@auth_bp.route('/test_login', methods=["GET"])
@jwt_required()
def test_login():
    return generate_response(200, {"message": get_jwt_identity()})


@auth_bp.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    identity = get_jwt_identity()
    access_token = create_access_token(identity=identity, expires_delta=False)
    return generate_response(200, {"access_token": access_token})
