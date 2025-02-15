# pylint: disable=cyclic-import, broad-exception-caught
"""This module define starting route."""

import importlib
import logging
from types import ModuleType

from flask import jsonify, request

from app import app
from app.modules import get_named_modules

for named_module in get_named_modules():
    try:
        module: ModuleType = importlib.import_module(
            f".modules.{named_module}.views", package="app"
        )
        api_route_path: str = named_module.replace("_", "-")
        app.register_blueprint(
            getattr(module, "blueprint"),
            url_prefix=f"/todo-api/{api_route_path}",
        )
    except Exception as e:
        pass


@app.route("/")
def index():
    """Base api route"""
    link_serializable = []
    links = app.url_map.iter_rules()
    for link in links:
        link_serializable.append(str(f"{link} {link.methods}"))
    return jsonify(Rotas=link_serializable)


@app.before_request
def log_request_data():
    """Add request data in log"""
    if request.is_json and "password" in request.json:
        request_info = {
            "request": request,
            "data_args": [request.args],
            "data_json": [request.json],
        }
    else:
        request_info = {
            "request": request,
            "data_args": [request.args],
        }

    log_message = f"Request info: {request_info}"
    logging.info(log_message)
