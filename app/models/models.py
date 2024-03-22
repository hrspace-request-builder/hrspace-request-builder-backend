from decimal import Decimal
from sqlalchemy import (
    ARRAY, Boolean, Integer, String
)
from sqlalchemy.orm import Mapped, mapped_column

from app.core.config import settings

from .base import Base


class GenericModel(Base):
    __abstract__ = True

    name: Mapped[str] = mapped_column(
        String(settings.name_max_len), unique=True, index=True
    )

    def __repr__(self) -> str:
        return f"\nid: {self.id}" f"\nname: {self.name}\n"


class Vacancy(GenericModel):
    salary_from: Mapped[Decimal] = mapped_column(
        Decimal(
            settings.decimal_precision,
            settings.decimal_scale
        )
    )
    salary_to: Mapped[Decimal] = mapped_column(
        Decimal(
            settings.decimal_precision,
            settings.decimal_scale
        )
    )
    conditions_description: Mapped[str] = mapped_column(
        String(settings.description_max_len)
    )
    hr_salary_model: Mapped[Integer] = mapped_column(Integer)
    hr_salary: Mapped[int] = mapped_column(
        Decimal(
            settings.decimal_precision,
            settings.decimal_scale
        )
    )
    employee_to_search: Mapped[int] = mapped_column(Integer)
    number_of_recruiters: Mapped[int] = mapped_column(Integer)
    when_work: Mapped[str] = mapped_column(
        String(settings.when_work_max_len))
    what_need: Mapped[str] = mapped_column(
        String(settings.what_need_max_len))
    additional_tasks: Mapped[list] = mapped_column(ARRAY(String))
    special_requirements: Mapped[str] = mapped_column(
        String(settings.requirements_max_len),
        default=''
    )
    show_info: Mapped[bool] = mapped_column(Boolean, default=False)

    def __repr__(self) -> str:
        return (
            f"\nsalary_from: {self.salary_from}"
            f"\nsalary_to: {self.salary_to}"
            f"\nconditions_description: {self.conditions_description}"
            f"\nhr_salary_model: {self.hr_salary_model}"
            f"\nhr_salary: {self.hr_salary}"
            f"\nemployee_to_search: {self.employee_to_search}"
            f"\nnumber_of_recruiters: {self.number_of_recruiters}"
            f"\nwhen_work: {self.when_work}"
            f"\nwhat_need: {self.what_need}"
            f"\nadditional_tasks: {self.additional_tasks}"
            f"\nspecial_requirements: {self.special_requirements}"
            f"\nshow_info: {self.show_info}\n"
        )


class City(GenericModel):
    pass
