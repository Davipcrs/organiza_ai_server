import os
from sqlalchemy import create_engine
# from dotenv import load_dotenv
from models.note import NoteModel
# load_dotenv()

_DATABASE_USER = os.getenv("DATABASE_USER")
_DATABASE_PWD = os.getenv("DATABASE_PWD")

_DATABASE_STRING_CONNECTION = f"postgresql+psycopg2://{
    _DATABASE_USER}:{_DATABASE_PWD}@localhost:5432/organiza_ai"

ENGINE = create_engine(_DATABASE_STRING_CONNECTION)


def initDatabase():
    eng = ENGINE
    NoteModel.__table__.create(bind=eng, checkfirst=True)
