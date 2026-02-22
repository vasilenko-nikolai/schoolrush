import re
from dataclasses import dataclass
from datetime import date
from typing import Final
from uuid import UUID

from app.domain.exceptions import EmailInvalidError

EMAIL_RE: Final = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


@dataclass(frozen=True)
class Email:
    value: str

    def __post_init__(self) -> None:
        if not EMAIL_RE.match(self.value):
            raise EmailInvalidError(self.value)

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return f"Email(value={self.value})"


@dataclass(frozen=True)
class PasswordRaw:
    value: str

    def __post_init__(self) -> None: ...


class Person:
    def __init__(
        self,
        *,
        person_id: UUID | None,
        hashed_password: str,
        email: Email,
        login: str | None = None,
        name: str | None = None,
        surname: str | None = None,
        verified: bool = False,
        birthday: date | None = None,
    ) -> None:
        self._new = False
        self.person_id = person_id
        self.name = name
        self.surname = surname
        self.hashed_password = hashed_password
        self.email = email
        self.verified = verified
        self.login = login
        self.birthday = birthday

    @property
    def person_id(self) -> UUID:
        if self._id is None:
            raise ValueError("Person is new, and not have id")
        return self._id

    @person_id.setter
    def person_id(self, person_id: UUID | None) -> None:
        self._new = False
        if person_id is None:
            self._new = True

        self._id = person_id

    @property
    def new(self) -> bool:
        return self._new

    def __eq__(self, value: object, /) -> bool:
        if not isinstance(value, Person):
            return False

        return value.person_id == self.person_id
