from decimal import Decimal
from pydantic import (
    BaseModel, ConfigDict,
    Field, field_validator
)
from typing import List, Optional

from app.core.config import settings
from .fields import name_field


class Base(BaseModel):
    id: int


class BaseOut(Base):
    model_config = ConfigDict(arbitrary_types_allowed=True, from_attributes=True)


class VacancyNamesOut(BaseOut):
    name: str = name_field("Название вакансии")


class CityOut(BaseOut):
    name: str = name_field("Название города")


class Specialization(Base):
    name: str = name_field("Программисты")


class Responsibilities(Base):
    name: str = name_field(
        "Разработка пользовательских интерфейсов для мобильных"
        "приложений с учетом лучших практик UX/UI дизайна."
    )


class Requirements(Base):
    name: str = name_field("Высшее образование в области дизайна")


class Conditions(Base):
    name: str = name_field("Оформление по ТК РФ")


class Salary(BaseModel):
    min: int
    max: int


class Data(BaseModel):
    specialization: Specialization
    salary: Salary
    responsibilities: list[Responsibilities]
    requirements: list[Requirements]
    conditions: list[Conditions]


class VacancyOut(BaseModel):
    id: int
    vacancy_name: Optional[str] 
    specialization: Optional[str]
    salary_from: Decimal = Field(ge=0)
    salary_to: Decimal = Field(ge=0)
    grade: str  
    experience: str  
    city: str  
    work_type: List[str]
    employment: str 
    registration_type: str  
    responsibilities: List[str]  
    responsibilities_description: str  
    requirements: List[str]  
    requirements_description: str  
    conditions: List[str]
    conditions_description: str
    hr_salary_model: int
    hr_salary: Decimal = Field(ge=0)
    employee_to_search: int
    number_of_recruiters: int
    when_work: str
    what_need: str
    additional_tasks: List[str]
    special_requirements: str
    show_info: bool = False

    @field_validator('salary_to')
    @classmethod
    def validate_salary_range(self, value, field):
        if value < self.salary_from:
            raise ValueError(
                'salary_to must be greater than or equal to salary_from')
        return value

    @field_validator('grade')
    @classmethod
    def validate_grade(cls, value):
        if value not in settings.grades:
            raise ValueError('Invalid grade')
        return value
    
    @field_validator('experience')
    @classmethod
    def validate_experience(cls, value):
        if value not in settings.experience_levels:
            raise ValueError('Invalid experience')
        return value

    @field_validator('work_type')
    @classmethod
    def validate_work_type(cls, value):
        if value not in settings.work_types:
            raise ValueError('Invalid work_type')
        return value

    @field_validator('employment')
    @classmethod
    def validate_employment(cls, value):
        if value not in settings.employment_types:
            raise ValueError('Invalid employment type')
        return value

    @field_validator('registration_type')
    @classmethod
    def validate_registration_type(cls, value):
        if value not in settings.registration_types:
            raise ValueError('Invalid registration type')
        return value

    @field_validator('number_of_recruiters')
    @classmethod
    def validate_number_of_recruiters(cls, value):
        if value not in settings.number_of_recruiters:
            raise ValueError('Invalid number of recruiters')
        return value

    @field_validator('hr_salary_model')
    @classmethod
    def validate_hr_salary_model(cls, value):
        if value not in settings.hr_salary_model:
            raise ValueError('Invalid hr_salary_model')
        return value

    @field_validator('when_work')
    @classmethod
    def validate_when_work(cls, value):
        if value not in settings.when_work_options:
            raise ValueError('Invalid when_work option')
        return value

    @field_validator('what_need')
    @classmethod
    def validate_what_need(cls, value):
        if value not in settings.what_need_options:
            raise ValueError('Invalid what_need option')
        return value
