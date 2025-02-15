"""This module is about exceptions."""

from http import HTTPStatus


class ErrorAbstract(Exception):
    """This class is about abstract error."""

    status_code: int = HTTPStatus.NOT_FOUND
    message: str = ""

    def __init__(self, message=None, status_code=None, payload=None):
        super(__class__, self).__init__(message)
        self.message = message or self.message
        self.status_code = status_code or self.status_code
        self.payload = payload

    def to_dict(self):
        """Transform error to dict."""
        exception = dict(self.payload or ())
        exception["message"] = self.message

        return exception


class WrongParameterException(ErrorAbstract):
    """This class is about wrong parameter error."""

    status_code: int = HTTPStatus.BAD_REQUEST
    message: str = "Parameter does not exist"


class WrongValueParameterException(ErrorAbstract):
    """This class is about wrong value parameter error."""

    status_code: int = HTTPStatus.BAD_REQUEST
    message: str = "Parameter value is wrong"


class SQLIntegrityErrorException(ErrorAbstract):
    """This class is about Integrity Error."""

    status_code: int = HTTPStatus.INTERNAL_SERVER_ERROR
    message: str = "One or more associated resources not found in Database."
