"""Config instance"""

import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

JSON_AS_ASCII = False
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = (
    f'postgresql+psycopg2://{os.environ["DB_USERNAME"]}'
    f':{os.environ["DB_PASSWORD"]}'
    f'@{os.environ["DB_HOST"]}'
    f':5432/{os.environ["DB_DATABASE"]}'
)
