from models.note import NoteModel
from database.database import ENGINE
from sqlalchemy.orm import Session
from sqlalchemy import select

from models.todo import TodoModel


def selectAllNotes():
    with Session(ENGINE) as session:
        stmt = select(NoteModel.int_id,
                      NoteModel.str_title,
                      NoteModel.str_desc,
                      NoteModel.str_created,
                      NoteModel.str_deadLine).order_by(NoteModel.int_id)

        rows = session.execute(statement=stmt)
        session.close()
        return rows.all()


def selectOneNote(id: int):
    with Session(ENGINE) as session:
        stmt = select(NoteModel.int_id,
                      NoteModel.str_title,
                      NoteModel.str_desc,
                      NoteModel.str_created,
                      NoteModel.str_deadLine).where(NoteModel.int_id == id)
        rows = session.execute(statement=stmt)
        session.close()
        return rows.all()


def selectAllTodos():
    with Session(ENGINE) as session:
        stmt = select(TodoModel.int_id, TodoModel.str_title).order_by(
            TodoModel.int_id)

        rows = session.execute(statement=stmt)
        session.close()
        return rows.all()


def selectOneTodo(id: int):
    with Session(ENGINE) as session:
        stmt = select(TodoModel.int_id, TodoModel.str_title).where(
            TodoModel.int_id == id)

        rows = session.execute(statement=stmt)
        session.close()
        return rows.all()
