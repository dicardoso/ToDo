"""Class for validating HTTP response codes"""
from http import HTTPStatus

from app.commom.exceptions.default_exceptions import (
    InternalServerErrorException,
    NotFoundException,
    ServiceUnavailableException,
    UnauthorizedException,
)


def validate_response_code(response, validators=None):
    """Method for validating HTTP response codes and raising their corresponding exceptions"""
    validations: dict = {
        HTTPStatus.UNAUTHORIZED: UnauthorizedException,
        HTTPStatus.NOT_FOUND: NotFoundException,
        HTTPStatus.SERVICE_UNAVAILABLE: ServiceUnavailableException,
        HTTPStatus.INTERNAL_SERVER_ERROR: InternalServerErrorException,
        HTTPStatus.OK: None,
    }

    if validators:
        validations.update(validators)

    validate_result = validations.get(response.status_code)

    if validate_result:
        raise validate_result
