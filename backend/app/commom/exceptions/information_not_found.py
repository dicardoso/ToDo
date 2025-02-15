"""Information not found module"""
from http import HTTPStatus

from app.core.exceptions_abstract import ErrorAbstract


class InformationNotFound(ErrorAbstract):
    """Information not found class"""

    status_code: int = HTTPStatus.NOT_FOUND
    message: str = "Information not found."
