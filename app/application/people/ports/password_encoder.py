from abc import ABC, abstractmethod

from app.domain.people import PasswordRaw


class PasswordEncoder(ABC):
    @abstractmethod
    def encode(self, password: PasswordRaw, dynamic_salt: str) -> str:
        raise NotImplementedError()
