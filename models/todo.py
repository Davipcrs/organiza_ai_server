from database.utils import BASE
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Integer, String, Text


class TodoModel(BASE):
    __tablename__ = "todos"
    int_id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True)
    str_title: Mapped[str] = mapped_column(Text())
    pass
