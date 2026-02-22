from datetime import date
from uuid import UUID

from sqlalchemy import String, text
from sqlalchemy.orm import Mapped, mapped_column

from .base import BaseOrm


class PeopleOrm(BaseOrm):
    __tablename__ = "people"

    id: Mapped[UUID]
    email: Mapped[str] = mapped_column(String(255), unique=True)
    password_hash: Mapped[str]
    login: Mapped[str | None] = mapped_column(String(30), unique=True)
    name: Mapped[str | None] = mapped_column(String(60))
    surname: Mapped[str | None] = mapped_column(String(60))
    birthday: Mapped[date | None]
    verified: Mapped[bool] = mapped_column(server_default=text("FALSE"))
