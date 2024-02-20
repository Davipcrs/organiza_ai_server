from database.utils import BASE
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Integer, String, Text, Boolean


class AppointmentModel(BASE):
    __tablename__ = "appointments"

    int_id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True)
    str_title: Mapped[str] = mapped_column(Text())
    str_desc: Mapped[str] = mapped_column(Text())
    str_start: Mapped[str] = mapped_column(String(100))
    str_end: Mapped[str] = mapped_column(String(100))
    int_color: Mapped[int] = mapped_column(Integer)
    bool_canceled: Mapped[bool] = mapped_column(Boolean)
