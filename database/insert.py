from models.note import NoteModel
from database.database import ENGINE
from sqlalchemy.orm import Session
from sqlalchemy import insert


def insertNote(str_title: str, str_desc: str | None = None, str_created: str | None = None, str_deadLine: str | None = None):
    """Insert note function. str_title is the only required parameter"""
    with Session(ENGINE) as session:
        stmt = insert(NoteModel).values(str_title=str_title,
                                        str_desc=str_desc,
                                        str_created=str_created,
                                        str_deadLine=str_deadLine)

        session.execute(statement=stmt)
        session.commit()
        session.close()

        return
