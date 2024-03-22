from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field

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
