from hashlib import sha256

from app.application.people.ports.password_encoder import PasswordEncoder
from app.domain.people import PasswordRaw
from app.infra.security.config import SecurityConfig


class PasswordSha256Encoder(PasswordEncoder):
    def __init__(
        self,
        config: SecurityConfig,
    ) -> None:
        self._config = config

    def encode(
        self,
        password: PasswordRaw,
        dynamic_salt: str = "",
    ) -> str:
        return sha256(
            sha256(
                f"{dynamic_salt}{password.value}{self._config.password_salt}".encode()
            )
            .hexdigest()
            .encode()
        ).hexdigest()
