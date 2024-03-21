from pydantic import BaseModel, ConfigDict, Field
from typing import List

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
    conditions_description: str
    hr_salary_model: int
    hr_salary: int
    employee_to_search: int
    number_of_recruiters: int
    when_work: str
    what_need: str
    additional_tasks: List[str]
    special_requirements: str
    show_info: bool = False
