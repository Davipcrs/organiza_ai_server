import os
from sqlalchemy import create_engine
# from dotenv import load_dotenv
from models.note import NoteModel
# load_dotenv()

_DATABASE_USER = os.getenv("DATABASE_USER")
_DATABASE_PWD = os.getenv("DATABASE_PWD")

_DATABASE_STRING_CONNECTION = "postgresql+psycopg2://{user}:{pwd}@localhost:5432/organiza_ai".format(
    user=_DATABASE_USER,
    pwd=_DATABASE_PWD
)

ENGINE = create_engine(_DATABASE_STRING_CONNECTION)


def initDatabase():
    eng = ENGINE
    NoteModel.__table__.create(bind=eng, checkfirst=True)
