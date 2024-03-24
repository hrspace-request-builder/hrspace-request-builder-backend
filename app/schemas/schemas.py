from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field, field_validator

from app.core.config import settings

from .fields import name_field


class Salary(BaseModel):
    min: Decimal = Field(default=1000.00, examples=[1000.00])
    max: Decimal = Field(default=100000.00, examples=[100000.00])


class Base(BaseModel):
    id: int


class Responsibility(Base):
    name: str = name_field(
        "Разработка пользовательских интерфейсов для мобильных"
        "приложений с учетом лучших практик UX/UI дизайна."
    )


class Requirement(Base):
    name: str = name_field("Высшее образование в области дизайна")


class Condition(Base):
    name: str = name_field("Условия труда")


class ShortSpecialization(Base):
    name: str = name_field("Мидл фронтенд разработчик")


class MidSpecialization(ShortSpecialization):
    category_id: int


class FullSpecialization(MidSpecialization):
    responsibilities: list[Responsibility]
    requirements: list[Requirement]


class BaseOut(Base):
    model_config = ConfigDict(
        arbitrary_types_allowed=True, from_attributes=True, extra="ignore"
    )


class VacancyNameOut(BaseOut):
    name: str = name_field("Название вакансии")


class CityOut(BaseOut):
    name: str = name_field("Название города")


class CategoryOut(BaseOut):
    name: str = name_field("Название сферы деятельности")
    specializations: list[ShortSpecialization]


class FullResponse(BaseModel):
    specialization: FullSpecialization
    salary: Salary
    conditions: list[Condition]


class VacancyOut(BaseModel):
    id: int
    vacancy_name: str | None
    specialization: str | None
    salary_from: Decimal = Field(ge=0)
    salary_to: Decimal = Field(ge=0)
    grade: str
    experience: str
    city: str
    work_type: list[str]
    employment: str
    registration_type: str
    responsibilities: list[str]
    responsibilities_description: str
    requirements: list[str]
    requirements_description: str
    conditions: list[str]
    conditions_description: str
    hr_salary_model: int
    hr_salary: Decimal = Field(ge=0)
    employee_to_search: int
    number_of_recruiters: int
    when_work: str
    what_need: str
    additional_tasks: list[str]
    special_requirements: str
    show_info: bool = False

    @field_validator("salary_to")
    @classmethod
    def validate_salary_range(self, value, field):
        if value < self.salary_from:
            raise ValueError("salary_to must be greater than or equal to salary_from")
        return value

    @field_validator("grade")
    @classmethod
    def validate_grade(cls, value):
        if value not in settings.grades:
            raise ValueError("Invalid grade")
        return value

    @field_validator("experience")
    @classmethod
    def validate_experience(cls, value):
        if value not in settings.experience_levels:
            raise ValueError("Invalid experience")
        return value

    @field_validator("work_type")
    @classmethod
    def validate_work_type(cls, value):
        if value not in settings.work_types:
            raise ValueError("Invalid work_type")
        return value

    @field_validator("employment")
    @classmethod
    def validate_employment(cls, value):
        if value not in settings.employment_types:
            raise ValueError("Invalid employment type")
        return value

    @field_validator("registration_type")
    @classmethod
    def validate_registration_type(cls, value):
        if value not in settings.registration_types:
            raise ValueError("Invalid registration type")
        return value

    @field_validator("number_of_recruiters")
    @classmethod
    def validate_number_of_recruiters(cls, value):
        if value not in settings.number_of_recruiters:
            raise ValueError("Invalid number of recruiters")
        return value

    @field_validator("hr_salary_model")
    @classmethod
    def validate_hr_salary_model(cls, value):
        if value not in settings.hr_salary_model:
            raise ValueError("Invalid hr_salary_model")
        return value

    @field_validator("when_work")
    @classmethod
    def validate_when_work(cls, value):
        if value not in settings.when_work_options:
            raise ValueError("Invalid when_work option")
        return value

    @field_validator("what_need")
    @classmethod
    def validate_what_need(cls, value):
        if value not in settings.what_need_options:
            raise ValueError("Invalid what_need option")
        return value
