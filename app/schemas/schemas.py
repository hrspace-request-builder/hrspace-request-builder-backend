from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field, field_validator

from app.core.config import settings

from .fields import field_examples, name_field


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


class VacancyIn(BaseModel):
    name: str = name_field("Название вакансии")
    # relation id
    specialization_id: int = field_examples(1)
    city_id: int = field_examples(1)
    # Numeric auto validation
    salary_from: Decimal = Field(ge=0, examples=[1000.00])
    salary_to: Decimal = Field(ge=0, examples=[2000.00])
    hr_salary: Decimal = Field(ge=0, examples=[1000.00])
    hr_salary_model: int = Field(ge=1, le=3, examples=[2])
    employee_to_search: int = Field(ge=1, examples=[2])
    number_of_recruiters: int = Field(ge=1, le=3, examples=[2])
    # Radio buttons - single value
    grade: str = name_field("middle")
    experience: str = name_field("неважно")
    employment: str = name_field("полная занятость")
    registration_type: str = name_field("самозанятость")
    when_work: str = name_field("Срочно")
    what_need: str = name_field("Резюме + результаты собеседования")
    # Checkboxes - multiple values
    work_types: list[str] = field_examples(settings.work_types)
    responsibilities_ids: list[int] = field_examples([1, 2, 3])
    requirements_ids: list[int] = field_examples([1, 2, 3])
    conditions_ids: list[int] = field_examples([1, 2, 3])
    additional_tasks: list[str] = field_examples(settings.vacancy_additional_tasks)
    # Произвольный текст
    responsibilities_description: str = name_field("Обязанности свое описание")
    requirements_description: str = name_field("Требования свое описание")
    conditions_description: str = name_field("Условия свое описание")
    special_requirements: str = name_field("Специальные требования свое описание")
    show_info: bool = Field(default=False)

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

    @field_validator("when_work")
    @classmethod
    def validate_when_work(cls, value):
        if value not in settings.vacancy_when_work_options:
            raise ValueError("Invalid when_work option")
        return value

    @field_validator("what_need")
    @classmethod
    def validate_what_need(cls, value):
        if value not in settings.vacancy_what_need_options:
            raise ValueError("Invalid what_need option")
        return value


class VacancyOut(Base, VacancyIn):
    pass
