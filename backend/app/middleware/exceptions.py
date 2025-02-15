"""Middleware Exception module"""

from http import HTTPStatus

from app.core.exceptions_abstract import ErrorAbstract


class MiddlewareBadAuthorizationHeaderException(ErrorAbstract):
    """Exception to Bad Authorization header"""

    message: str = "Bad Authorization header. Expected value 'Bearer JWT'"
    status_code: int = HTTPStatus.UNAUTHORIZED


class MiddlewareExpiredAuthorizationException(ErrorAbstract):
    """Exception to Expired authorization"""

    message: str = "Expired authorization"
    status_code: int = HTTPStatus.UNAUTHORIZED


class MiddlewareTokenInvalidFormatException(ErrorAbstract):
    """Exception to Token with invalid format"""

    message: str = "Token with invalid format"
    status_code: int = HTTPStatus.UNAUTHORIZED


class MiddlewareAuthorizationHeaderNotFoundException(ErrorAbstract):
    """Exception to Authorization header not found"""

    message: str = "Authorization header not found"
    status_code: int = HTTPStatus.NOT_FOUND
