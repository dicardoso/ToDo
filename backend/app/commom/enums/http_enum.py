# pylint: disable=invalid-str-returned
"""HTTP VERB Module."""

from enum import Enum


class HttpVerbENUM(Enum):
    """HTTP VERB ENUM"""

    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    GET = "GET"
    OPTIONS = "OPTIONS"

    def __str__(self):
        return self.value


class StateENUM(Enum):
    """ENUM STATE"""

    SUCCESS = "success"
    ERROR = "error"

    def __str__(self):
        return self.value
