from models.appointment import AppointmentModel
from models.note import NoteModel
from database.database import ENGINE
from sqlalchemy.orm import Session
from sqlalchemy import insert

from models.todo import TodoModel


def insertNote(str_title: str, str_desc: str | None = None, str_created: str | None = None, str_deadLine: str | None = None):
    """Insert note function. str_title is the only required parameter"""
    with Session(ENGINE) as session:
        stmt = insert(NoteModel).values(str_title=str_title,
                                        str_desc=str_desc,
                                        str_created=str_created,
                                        str_deadLine=str_deadLine).returning(NoteModel.int_id)

        rows = session.execute(statement=stmt)
        session.commit()
        session.close()

        return rows.all()


def insertTodo(str_title: str):
    with Session(ENGINE) as session:
        stmt = insert(TodoModel).values(
            str_title=str_title).returning(TodoModel.int_id)

        rows = session.execute(statement=stmt)
        session.commit()
        session.close()

        return rows.all()


def insertAppointment(str_title: str, str_start: str, str_end: str, str_desc: str | None = None, int_color: str | None = None, bool_canceled: bool | None = None):
    with Session(ENGINE) as session:
        stmt = insert(AppointmentModel).values(str_title=str_title,
                                               str_desc=str_desc,
                                               str_start=str_start,
                                               str_end=str_end,
                                               int_color=int_color,
                                               bool_canceled=bool_canceled).returning(AppointmentModel.int_id)

        rows = session.execute(statement=stmt)
        session.commit()
        session.close()

        return rows.all()
