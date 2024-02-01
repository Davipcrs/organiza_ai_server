import os
from sqlalchemy import create_engine
from dotenv import load_dotenv, find_dotenv
from models.note import NoteModel
from models.todo import TodoModel
load_dotenv(find_dotenv(), override=True)

_DATABASE_USER = os.getenv("DATABASE_USER")
_DATABASE_PWD = os.getenv("DATABASE_PWD")

_DATABASE_STRING_CONNECTION = "postgresql+psycopg2://{user}:{pwd}@192.168.0.51:5432/organiza_ai".format(
    user=_DATABASE_USER,
    pwd=_DATABASE_PWD
)

ENGINE = create_engine(_DATABASE_STRING_CONNECTION)


def initDatabase():
    eng = ENGINE
    NoteModel.__table__.create(bind=eng, checkfirst=True)
    TodoModel.__table__.create(bind=eng, checkfirst=True)
