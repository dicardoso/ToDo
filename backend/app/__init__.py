# pylint: disable=wrong-import-position, wrong-import-order

"""This module initialize de app."""

import logging
from os import environ

from flask import Flask
from flask_cors import CORS
from flask_injector import FlaskInjector
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_swagger_ui import get_swaggerui_blueprint
from sqlalchemy import MetaData
from werkzeug.middleware.proxy_fix import ProxyFix

from app import modules

from .db_config.constraint_convention import constraint_convention
from .seeds.seeder import Seeds

if environ.get("FLASK_ENV") != "test":
    from .middleware.middleware import Middleware

console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
logging.getLogger("").addHandler(console)

app = Flask(__name__, instance_relative_config=True)
print(app.root_path)
app.config.from_pyfile("config.py")
app.config["JSON_AS_ASCII"] = False

CORS(app)

# DataBase Instance
metadata = MetaData(naming_convention=constraint_convention())
db = SQLAlchemy(app, metadata=metadata, session_options={"autoflush": False})
migrate = Migrate(app, db)

### swagger specific ###

SWAGGER_URL = f'{environ.get("PREFIX_URL")}/swagger'

# if environ.get("FLASK_ENV") == "production":
#     API_URL = f'{environ.get("PREFIX_URL")}/static/swagger.json'
# else:
#     API_URL = "/static/swagger.json"
API_URL = "/static/swagger.json"
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL, API_URL, config={"app_name": "ToDo"}
)

app.register_blueprint(swaggerui_blueprint)
### end swagger specific ###

app.wsgi_app = ProxyFix(app.wsgi_app)

if environ.get("FLASK_ENV") != "test":
    app.wsgi_app = Middleware(app.wsgi_app)

seeder = Seeds(db, modules)


@app.cli.command()
def seed():
    """Seed datas from here"""
    seeder.run()


# pylint: disable=wrong-import-position, wrong-import-order
from app.core import routes
from app.modules import *

FlaskInjector(app)

if __name__ == "__main__":
    app.run(port=4020)
