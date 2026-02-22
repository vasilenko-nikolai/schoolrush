from abc import ABC, abstractmethod
from uuid import UUID

from app.domain.people import Email, Person


class PeopleRepo(ABC):
    @abstractmethod
    async def find_by_email_or_login(self, email_or_login: str) -> Person | None:
        raise NotImplementedError()

    @abstractmethod
    async def find_by_email(self, email: Email) -> Person | None:
        raise NotImplementedError()

    @abstractmethod
    async def save(self, person: Person) -> UUID:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_id(self, person_id: UUID) -> Person:
        raise NotImplementedError()

    @abstractmethod
    async def find_by_id(self, person_id: UUID) -> Person | None:
        raise NotImplementedError()
