from models.note import NoteModel
from database.database import ENGINE
from sqlalchemy.orm import Session
from sqlalchemy import update


def updateNote(note):
    with Session(ENGINE) as session:
        stmt = ""

        session.execute(statement=stmt)
        session.commit()
        session.close()
        return
