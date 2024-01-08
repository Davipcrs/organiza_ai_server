from database.utils import BASE
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Integer, String, Text


class NoteModel(BASE):
    __tablename__ = "notes"

    int_id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True)
    str_title: Mapped[str] = mapped_column(Text())
    str_desc: Mapped[str] = mapped_column(Text())
    str_created: Mapped[str] = mapped_column(String(100))
    str_deadLine: Mapped[str] = mapped_column(String(100))
