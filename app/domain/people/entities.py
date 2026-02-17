from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass
class Person:
    id: UUID
    email: str
    name: str
    surname: str
    birthday: datetime | None = None
