from sqlalchemy.orm import DeclarativeBase
from database.database import ENGINE
from models.note import NoteModel

# THIS CLASS IS USED IN THE MODELS TABLES FOR INHERITANCE


class BASE(DeclarativeBase):
    pass


def initDatabase():
    eng = ENGINE
    NoteModel.__table__.create(bind=eng, checkfirst=True)
