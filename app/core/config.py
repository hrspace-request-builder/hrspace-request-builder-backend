from pydantic import SecretStr  # EmailStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )

    # constants
    URL_PREFIX: str = "/api/v1/"
    DEFAULT_STR: str = "To be implemented in .env file"
    # SUPER_ONLY: str = '__Только для суперюзеров:__ '
    # AUTH_ONLY: str = '__Только для авторизованных пользователей:__ '
    ALL_USERS: str = "__Для всех пользователей:__ "

    # Application settings
    app_title: str = f"App title {DEFAULT_STR}"
    app_description: str = f"App description {DEFAULT_STR}"
    secret_key: SecretStr = f"Secret key {DEFAULT_STR}"

    # DB settings
    postgres_user: str  # = "postgres"
    postgres_password: str  # = "postgres"
    db_host: str  # = "db"
    db_port: str  # = "5432"
    postgres_db: str  # = "postgres"

    @property
    def database_url(self) -> str:
        return (
            f"postgresql+asyncpg://"
            f"{self.postgres_user}:{self.postgres_password}@"
            f"{self.db_host}:{self.db_port}/{self.postgres_db}"
        )


settings = Settings()
