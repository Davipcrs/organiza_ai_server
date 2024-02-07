import os
from sqlalchemy import Engine, create_engine
# from dotenv import load_dotenv, find_dotenv
from models.note import NoteModel
from models.todo import TodoModel
# Docker mods
# load_dotenv(find_dotenv(), override=True)

_DATABASE_USER = os.getenv("DATABASE_USER")
_DATABASE_PWD = os.getenv("DATABASE_PWD")
_DATABASE_HOST = os.getenv("DATABASE_HOST")
_DATABASE_PORT = os.getenv("DATABASE_PORT")

_DATABASE_STRING_CONNECTION = "postgresql+psycopg2://{user}:{pwd}@{host}:{port}/organiza_ai".format(
    user=_DATABASE_USER,
    pwd=_DATABASE_PWD,
    host=_DATABASE_HOST,
    port=_DATABASE_PORT
)

ENGINE = create_engine(_DATABASE_STRING_CONNECTION)

# while not isinstance(ENGINE, Engine):


def initDatabase():
    eng = ENGINE
    NoteModel.__table__.create(bind=eng, checkfirst=True)
    TodoModel.__table__.create(bind=eng, checkfirst=True)
