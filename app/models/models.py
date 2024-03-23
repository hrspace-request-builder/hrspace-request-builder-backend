from decimal import Decimal
from sqlalchemy import (
    ARRAY, Boolean, Integer, String, ForeignKey
)
from sqlalchemy.orm import (
    Mapped, mapped_column, relationship
)

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
    __tablename__ = "vacancies"
    vacancy_name_id: Mapped[int] = mapped_column(
         ForeignKey("vacancy_name.id"))
    vacancy_name: Mapped["VacancyName"] = relationship("VacancyName")
    specialization_id: Mapped[int] = mapped_column(
        ForeignKey("specializations.id")
    )
    specialization: Mapped["Specialization"] = relationship(
        "Specialization"
    )
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
    grade: Mapped[str] =  mapped_column(
        String(settings.grade_max_len))
    experience: Mapped[str] = mapped_column(
        String(settings.experience_max_len))
    city_id: Mapped[int] = mapped_column(ForeignKey("cities.id"))
    city: Mapped["City"] = relationship("City")
    work_type: Mapped[list] = mapped_column(ARRAY(String))
    employment: Mapped[str] = mapped_column(
        String(settings.employment_max_len))
    registration_type: Mapped[str] = mapped_column(
        String(settings.reg_type_max_len))
    responsibilities: Mapped[list["Responsibility"]] = relationship(
        "Responsibility", secondary="vacancy_responsibilities",
        backref="vacancies"
    )
    responsibilities_description: Mapped[str] = mapped_column(
        String(settings.description_max_len)
    )
    requirements: Mapped[list["Requirement"]] = relationship(
        "Requirement", secondary="vacancy_requirements",
        backref="vacancies"
    )
    requirements_description: Mapped[str] = mapped_column(
        String(settings.description_max_len)
    )
    conditions: Mapped[list["Condition"]] = relationship(
        "Condition", secondary="vacancy_conditions",
        backref="vacancies"
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
            f"\nvacancy_name: {self.vacancy_name}"
            f"\nspecialization: {self.specialization}"
            f"\nsalary_from: {self.salary_from}"
            f"\nsalary_to: {self.salary_to}"
            f"\ngrade: {self.grade}"
            f"\nexperience: {self.experience}"
            f"\ncity: {self.city}"
            f"\nwork_type: {self.work_type}"
            f"\nemployment: {self.employment}"
            f"\nregistration_type: {self.registration_type}"
            f"\nresponsibilities: {self.responsibilities}"
            f"\nresponsibilities_description: {self.responsibilities_description}"
            f"\nrequirements: {self.requirements}"
            f"\nrequirements_description: {self.requirements_description}"
            f"\nconditions: {self.conditions}"
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
