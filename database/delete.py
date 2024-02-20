from models.appointment import AppointmentModel
from models.note import NoteModel
from database.database import ENGINE
from sqlalchemy.orm import Session
from sqlalchemy import delete

from models.todo import TodoModel


def deleteNote(id: int):
    with Session(ENGINE) as session:
        stmt = delete(NoteModel).where(NoteModel.int_id == id)

        session.execute(statement=stmt)
        session.commit()
        session.close()
        return


def deleteTodo(id: int):
    with Session(ENGINE) as session:
        stmt = delete(TodoModel).where(TodoModel.int_id == id)

        session.execute(statement=stmt)
        session.commit()
        session.close()
        return


def deleteAppointment(id: int):
    with Session(ENGINE) as session:
        stmt = delete(AppointmentModel).where(AppointmentModel.int_id == id)

        session.execute(statement=stmt)
        session.commit()
        session.close()
        return
