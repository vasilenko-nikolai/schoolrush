from uuid import UUID

from sqlalchemy import insert, or_, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.application.people.ports import PeopleRepo
from app.domain.people import Email, Person
from app.infra.db.models import PeopleOrm


def map_person_orm_to_person(person_orm: PeopleOrm) -> Person:
    return Person(
        person_id=person_orm.id,
        email=Email(person_orm.email),
        hashed_password=person_orm.password_hash,
        login=person_orm.login,
        name=person_orm.name,
        surname=person_orm.surname,
        verified=person_orm.verified,
        birthday=person_orm.birthday,
    )


class PeopleOrmRepo(PeopleRepo):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def save(self, person: Person) -> UUID:
        if person.new:
            return await self._create_person(person)
        return await self._update_person(person)

    async def _create_person(self, person: Person) -> UUID:
        query = (
            insert(PeopleOrm)
            .values(
                name=person.name,
                surname=person.surname,
                email=person.email.value,
                password_hash=person.hashed_password,
                login=person.login,
                birthday=person.birthday,
            )
            .returning(PeopleOrm.id)
        )
        result = await self._session.execute(query)
        return result.scalar_one()

    async def _update_person(self, person: Person) -> UUID:
        query = (
            update(PeopleOrm)
            .values(
                name=person.name,
                surname=person.surname,
                email=person.email.value,
                password_hash=person.hashed_password,
                login=person.login,
                birthday=person.birthday,
            )
            .where(PeopleOrm.id == person.person_id)
            .returning(PeopleOrm.id)
        )
        result = await self._session.execute(query)
        return result.scalar_one()

    async def find_by_email_or_login(self, email_or_login: str) -> Person | None:
        query = select(PeopleOrm).where(
            or_(PeopleOrm.login == email_or_login, PeopleOrm.email == email_or_login)
        )
        result = await self._session.execute(query)
        person_orm = result.scalar_one_or_none()

        if person_orm is None:
            return person_orm

        return map_person_orm_to_person(person_orm)

    async def find_by_email(self, email: Email) -> Person | None:
        query = select(PeopleOrm).where(PeopleOrm.email == email.value)
        result = await self._session.execute(query)
        person_orm = result.scalar_one_or_none()

        if person_orm is None:
            return person_orm

        return map_person_orm_to_person(person_orm)

    async def get_by_id(self, person_id: UUID) -> Person:
        query = select(PeopleOrm).where(PeopleOrm.id == person_id)
        result = await self._session.execute(query)
        person_orm = result.scalar_one()
        return map_person_orm_to_person(person_orm)

    async def find_by_id(self, person_id: UUID) -> Person | None:
        query = select(PeopleOrm).where(PeopleOrm.id == person_id)
        result = await self._session.execute(query)
        person_orm = result.scalar_one_or_none()
        if person_orm is None:
            return person_orm

        return map_person_orm_to_person(person_orm)
