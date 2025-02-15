from app.extensions import db
from app.modules.auth.models import User


class UserRepository:
    @staticmethod
    def get_user_by_email(email: str):
        return User.query.filter_by(email=email).first()
