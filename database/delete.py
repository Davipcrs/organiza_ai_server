from models.note import NoteModel
from database.database import ENGINE
from sqlalchemy.orm import Session
from sqlalchemy import delete


def deleteNote(id: int):
    with Session(ENGINE) as session:
        stmt = delete(NoteModel).where(NoteModel.int_id == id)

        session.execute(statement=stmt)
        session.commit()
        session.close()
        return
