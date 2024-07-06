from werkzeug.security import generate_password_hash, check_password_hash

from src.main.error_handlers import WrongPasswordException
from src.main.models.daos import users_dao
from src.main.models.schemas import user_authentication_schema


class UsersService:
    def create_user(self, data: dict):
        data['password_hash'] = generate_password_hash(data.pop('password'))
        user_info = users_dao.persist(data, user_authentication_schema)
        return user_info

    def login_user(self, data: dict):
        user_info = users_dao.get_by_username_for_login(data['username'])
        if not check_password_hash(user_info.pop('password_hash'), data['password']):
            raise WrongPasswordException("Wrong password")
        return user_info


users_service = UsersService()
