"""General exceptions to be used by application"""
from http import HTTPStatus

from app.core.exceptions_abstract import ErrorAbstract


class UnauthorizedException(ErrorAbstract):
    """This class is about unauthorized error."""

    status_code: int = HTTPStatus.UNAUTHORIZED
    message: str = "Invalid credentials or insufficient permissions."


class NotFoundException(ErrorAbstract):
    """This class is about not found error."""

    status_code: int = HTTPStatus.NOT_FOUND
    message: str = "The requested URL or resource ID does not exist."


class InternalServerErrorException(ErrorAbstract):
    """This class is about internal server error."""

    status_code: int = HTTPStatus.INTERNAL_SERVER_ERROR
    message: str = "An internal server error has occurred."


class RequestAuthServerException(ErrorAbstract):
    """Error on auth server"""

    status_code: int = HTTPStatus.NOT_ACCEPTABLE
    message: str = "Request to Auth Server return error."


class ServiceUnavailableException(ErrorAbstract):
    """This class is about service unavailable error."""

    status_code: int = HTTPStatus.SERVICE_UNAVAILABLE
    message: str = "Application currently unavailable."


class AuthAppUnavailableException(ErrorAbstract):
    """Exception for when Auth server is unavailable"""

    status_code: int = HTTPStatus.SERVICE_UNAVAILABLE
    message: str = "Failed to establish a connection with SmartAuth api."


class ConfigurationNotExistException(ErrorAbstract):
    """
    Exception class for when there is no Configuration saved in the database
    """

    status_code: int = HTTPStatus.INTERNAL_SERVER_ERROR
    message = "Could not find configuration for authentication."
