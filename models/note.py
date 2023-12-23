from database.utils import BASE
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Integer, String
from pydantic import BaseModel


class NoteModel(BASE):
    __tablename__ = "notes"

    int_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    str_title: Mapped[str] = mapped_column(String())
    str_desc: Mapped[str] = mapped_column(String())
    str_created: Mapped[str] = mapped_column(String())
    str_deadLine: Mapped[str] = mapped_column(String())
