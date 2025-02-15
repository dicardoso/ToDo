"""This module is middleware of todo api."""

import os
from http import HTTPStatus
from typing import List

import jwt
from flask import Flask, Request, Response

from app.commom.enums.http_enum import HttpVerbENUM

from .exceptions import (
    MiddlewareAuthorizationHeaderNotFoundException,
    MiddlewareBadAuthorizationHeaderException,
    MiddlewareExpiredAuthorizationException,
    MiddlewareTokenInvalidFormatException,
)


class Middleware:
    """This class is middleware."""

    ALLOWED_TOKEN_SIZE: int = 2
    ALLOWED_SCHEME: str = "Bearer"
    AUTHENTICATION_URI: str = f'{os.environ.get("PREFIX_URL")}/auth/'

    def __init__(self, app: Flask):
        self.app = app

    def __call__(self, environ: dict, start_response):
        request: Request = Request(environ)

        uri_exceptions_swagger: List = [
            "/swagger/",
            "/static/swagger/",
            "/swagger/index.css",
            "/swagger/swagger-ui.css",
            "/swagger/swagger-ui-bundle.js",
            "/swagger/swagger-ui-standalone-preset.js",
            "/swagger/favicon-32x32.png",
            "/swagger/favicon-16x16.png",
            "/swagger/swagger-ui.css.map",
            "/swagger/swagger-ui-bundle.js.map",
            "/swagger/swagger-ui-standalone-preset.js.map",
        ]

        exceptions_swagger = [
            f'{os.environ.get("PREFIX_URL")}{uri}' for uri in uri_exceptions_swagger
        ]

        if (
            request.path in exceptions_swagger
            or request.path == "/static/swagger.json"
            or request.path == self.AUTHENTICATION_URI
            or request.method == HttpVerbENUM.OPTIONS.value
        ):
            return self.app(environ, start_response)

        res: Response = Response(mimetype="text", status=HTTPStatus.UNAUTHORIZED)
        authorization: str = request.headers.get("Authorization")

        if authorization and authorization is not None:
            auth_list: List[str] = authorization.split(" ")

            if (not len(auth_list) == self.ALLOWED_TOKEN_SIZE) or (
                auth_list[0] != self.ALLOWED_SCHEME
            ):
                res.response = MiddlewareBadAuthorizationHeaderException.message

                return res(environ, start_response)

            try:
                token = jwt.decode(
                    jwt=auth_list[1],
                    key=os.environ["SECRET_KEY"],
                    algorithms=["HS256"],
                )
                user: dict = token["user"]
                environ["user_id"]: int = user["id"]
                return self.app(environ, start_response)

            except jwt.ExpiredSignatureError:
                res.response = MiddlewareExpiredAuthorizationException.message

                return res(environ, start_response)

            except jwt.exceptions.DecodeError:
                res.response = MiddlewareTokenInvalidFormatException.message
                return res(environ, start_response)

        else:
            res.response = MiddlewareAuthorizationHeaderNotFoundException.message

            return res(environ, start_response)
