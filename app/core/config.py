from pydantic import SecretStr  # EmailStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )

    # constants
    URL_PREFIX: str = "/api/v1/"
    DEFAULT_STR: str = "To be implemented in .env file"
    ALL_USERS: str = "__Для всех пользователей:__ "

    # Application settings
    app_title: str = f"App title {DEFAULT_STR}"
    app_description: str = f"App description {DEFAULT_STR}"
    secret_key: SecretStr = f"Secret key {DEFAULT_STR}"
    name_max_len: int = 256

    # DB settings
    postgres_user: str
    postgres_password: str
    db_host: str
    db_port: str
    postgres_db: str

    # vacancy settings
    grade_max_len: int = 6
    grades: tuple[str, ...] = ("middle", "junior", "senior", "lead")
    experience_levels: tuple[str, ...] = ("1-3 года", "неважно", "нет опыта", "3-6 лет")
    work_types: tuple[str, ...] = ("удаленная работа", "офис", "гибрид")
    employment_types: tuple[str, ...] = (
        "частичная",
        "полная занятость",
        "посменно",
        "другое",
    )
    registration_types: tuple[str, ...] = ("ИП", "ТК РФ", "самозанятость", "ГПХ")
    experience_max_len: int = 9
    employment_max_len: int = 16
    reg_type_max_len: int = 13
    decimal_precision: int = 10
    decimal_scale: int = 2
    description_max_len: int = 512
    number_of_recruiters: tuple[int, ...] = (1, 2, 3)
    hr_salary_model: tuple[int, ...] = (0, 1, 2)
    when_work_max_len: int = 20
    what_need_max_len: int = 100
    vacancy_when_work_options: tuple[str, ...] = (
        "Срочно",
        "Не очень срочно",
        "Времени достаточно",
    )
    vacancy_additional_tasks: tuple[str, ...] = (
        "тестирование кандидатов",
        "предварительное собеседование",
        "формирование отчёта по поиску",
        "подготовка рекомендаций по онбордингу",
    )
    vacancy_what_need_options: tuple[str, ...] = (
        "Только резюме",
        "Резюме + результаты собеседования",
    )
    requirements_max_len: int = 2000

    @property
    def database_url(self) -> str:
        return (
            f"postgresql+asyncpg://"
            f"{self.postgres_user}:{self.postgres_password}@"
            f"{self.db_host}:{self.db_port}/{self.postgres_db}"
        )


settings = Settings()
