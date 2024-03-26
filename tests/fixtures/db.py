from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.pool import NullPool


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )
    # defaults needed for GitHub Action tests
    postgres_user_test: str = "postgres"
    postgres_password_test: str = "postgrespw"
    db_host_test: str = "0.0.0.0"
    db_port_test: str = "5432"
    postgres_db_test: str = "postgres"

    @property
    def test_db_url(self) -> str:
        return (
            f"postgresql+asyncpg://"
            f"{self.postgres_user_test}:{self.postgres_password_test}@"
            f"{self.db_host_test}:{self.db_port_test}/{self.postgres_db_test}"
        )


test_db_settings = Settings()

test_engine = create_async_engine(test_db_settings.test_db_url, poolclass=NullPool)
TestingSessionLocal = async_sessionmaker(
    test_engine, expire_on_commit=False, autocommit=False, autoflush=False
)
