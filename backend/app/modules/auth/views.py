from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from app.modules.auth.services import AuthService

blueprint = Blueprint("auth", __name__)


@blueprint.route("/login", methods=["POST"])
def login():
    data = request.json
    token = AuthService.authenticate(data.get("email"), data.get("password"))

    if token:
        return jsonify({"access_token": token}), 200
    return jsonify({"error": "Credenciais inválidas"}), 401
