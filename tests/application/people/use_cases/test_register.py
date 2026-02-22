import uuid
from unittest.mock import AsyncMock, Mock

import pytest

from app.application.people.exceptions import PersonAlreadyExistsError
from app.application.people.ports import PasswordEncoder, PeopleRepo
from app.application.people.use_cases import PersonRegisterUseCase
from app.domain.people import Email, PasswordRaw, Person


@pytest.fixture()
def people_repo() -> PeopleRepo:
    return AsyncMock(spec=PeopleRepo)


@pytest.fixture()
def password_encoder() -> PasswordEncoder:
    return Mock(spec=PasswordEncoder)


@pytest.fixture()
def person_register_use_case(
    people_repo: PeopleRepo, password_encoder: PasswordEncoder
) -> PersonRegisterUseCase:
    return PersonRegisterUseCase(people_repo, password_encoder)


async def test_success_register(
    person_register_use_case: PersonRegisterUseCase,
    people_repo: AsyncMock,
    password_encoder: Mock,
) -> None:
    raw_password = "<RAW_PASSWORD>"
    encoded_password = "<ENCODED_PASSWORD>"
    email_str = "test@schoolrush.local"
    person_id = uuid.uuid4()

    people_repo.find_by_email.return_value = None
    password_encoder.encode.return_value = encoded_password
    people_repo.save.return_value = person_id
    people_repo.get_by_id.return_value = Person(
        person_id=person_id,
        hashed_password=encoded_password,
        email=Email(email_str),
    )
    await person_register_use_case.execute(email_str, raw_password)

    people_repo.find_by_email.assert_awaited_once_with(Email(email_str))
    password_encoder.encode.assert_called_once_with(PasswordRaw(raw_password))
    people_repo.save.assert_awaited_once()

    called_save_person = people_repo.save.call_args[0][0]
    assert called_save_person.hashed_password == encoded_password
    people_repo.get_by_id.assert_awaited_once_with(person_id)


async def test_already_exists_register(
    person_register_use_case: PersonRegisterUseCase,
    people_repo: AsyncMock,
    password_encoder: Mock,
) -> None:
    exists_email = "testemail@schoolrush.local"
    raw_password = "testpassword"
    exists_person = Person(
        person_id=None,
        hashed_password="Encdoede password",
        email=Email(exists_email),
    )

    people_repo.find_by_email.return_value = exists_person

    with pytest.raises(PersonAlreadyExistsError):
        await person_register_use_case.execute(exists_email, raw_password)

    people_repo.save.assert_not_called()
    password_encoder.encode.assert_not_called()
