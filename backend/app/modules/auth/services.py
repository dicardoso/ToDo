from app.modules.auth.repository import UserRepository
from flask_jwt_extended import create_access_token


class AuthService:
    @staticmethod
    def authenticate(email: str, password: str):
        user = UserRepository.get_user_by_email(email)
        if user and user.check_password(password):
            return create_access_token(identity=user.id)
        return None
