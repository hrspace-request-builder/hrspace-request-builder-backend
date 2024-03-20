from pydantic import BaseModel, ConfigDict

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
