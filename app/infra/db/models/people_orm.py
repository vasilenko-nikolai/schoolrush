from datetime import date

from fastapi_users.db import SQLAlchemyBaseUserTableUUID
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .base import BaseOrm


class PeopleOrm(SQLAlchemyBaseUserTableUUID, BaseOrm):
    __tablename__ = "people"

    name: Mapped[str] = mapped_column(String(60))
    surname: Mapped[str] = mapped_column(String(60))
    login: Mapped[str] = mapped_column(String(30))
    birthday: Mapped[date | None]
