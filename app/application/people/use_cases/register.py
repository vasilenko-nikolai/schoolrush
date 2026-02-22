from app.application.people.exceptions import PersonAlreadyExistsError
from app.application.people.ports import PasswordEncoder, PeopleRepo
from app.domain.people import Email, PasswordRaw, Person


class PersonRegisterUseCase:
    def __init__(
        self,
        people_repo: PeopleRepo,
        password_encoder: PasswordEncoder,
    ) -> None:
        self._people_repo = people_repo
        self._password_encoder = password_encoder

    async def execute(
        self,
        email_str: str,
        password_str: str,
    ) -> Person:
        email = Email(email_str)
        person_exists = await self._people_repo.find_by_email(email)
        if person_exists:
            raise PersonAlreadyExistsError("email", person_exists.email.value)

        password_raw = PasswordRaw(password_str)
        hash_password = self._password_encoder.encode(password_raw, email_str)
        new_person = Person(person_id=None, email=email, hashed_password=hash_password)
        person_id = await self._people_repo.save(new_person)
        return await self._people_repo.get_by_id(person_id)
