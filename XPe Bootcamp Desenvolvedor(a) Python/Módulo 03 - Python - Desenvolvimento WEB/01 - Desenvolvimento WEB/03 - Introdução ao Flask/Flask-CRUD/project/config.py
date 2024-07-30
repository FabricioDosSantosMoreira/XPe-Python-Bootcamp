import os

SECRET_KEY = os.urandom(32)
DEBUG = True

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "default_database.db")
SQLALCHEMY_TRACK_MODIFICATIONS = False
