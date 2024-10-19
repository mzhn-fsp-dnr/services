"""App configuration."""

from typing import List
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Settings class.
    """

    model_config = SettingsConfigDict(env_file=".env")

    PG_USER: str
    PG_PASS: str
    PG_HOST: str
    PG_PORT: int
    PG_NAME: str

    ALLOWED_ORIGINS: List[str]
    ALLOW_CREDENTIALS: bool
    ALLOW_METHODS: List[str]
    ALLOW_HEADERS: List[str]

    APP_DEBUG: bool
    APP_VERSION: str
    APP_PORT: int

    def database_link(self):
        return f"postgresql+psycopg2://{self.PG_USER}:{self.PG_PASS}@{self.PG_HOST}:{self.PG_PORT}/{self.PG_NAME}?sslmode=disable"
