from models.appointment import AppointmentModel
from models.note import NoteModel
from database.database import ENGINE
from sqlalchemy.orm import Session
from sqlalchemy import update

from models.todo import TodoModel


def updateNote(int_id: int, str_title: str, str_desc: str | None = None, str_created: str | None = None, str_deadLine: str | None = None):
    with Session(ENGINE) as session:
        stmt = update(NoteModel).values(str_title=str_title,
                                        str_desc=str_desc,
                                        str_created=str_created,
                                        str_deadLine=str_deadLine).where(NoteModel.int_id == int_id)

        session.execute(statement=stmt)
        session.commit()
        session.close()
        return


def updateTodo(int_id: int, str_title: str):
    with Session(ENGINE) as session:
        stmt = update(TodoModel).values(
            int_id=int_id, str_title=str_title).where(TodoModel.int_id == int_id)
        session.execute(statement=stmt)
        session.commit()
        session.close()
        return


def updateAppointment(int_id: int, str_title: str, str_start: str, str_end: str, str_desc: str | None = None, int_color: str | None = None, bool_canceled: bool | None = None):
    with Session(ENGINE) as session:
        stmt = update(AppointmentModel).values(str_title=str_title,
                                               str_desc=str_desc,
                                               str_start=str_start,
                                               str_end=str_end,
                                               int_color=int_color,
                                               bool_canceled=bool_canceled).where(AppointmentModel.int_id == int_id)

    session.execute(statement=stmt)
    session.commit()
    session.close()
    return
