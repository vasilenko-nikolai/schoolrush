from pydantic_settings import BaseSettings, SettingsConfigDict


class DbConfig(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="DB_")

    HOST: str
    PORT: int
    USER: str
    PASSWORD: str
    NAME: str

    @property
    def async_url(self) -> str:
        return f"postgresql+asyncpg://{self.USER}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.NAME}"

    @property
    def sync_url(self) -> str:
        return f"postgresql+psycopg2://{self.USER}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.NAME}"


db_config = DbConfig()  # type: ignore
