from decimal import Decimal

from sqlalchemy import Boolean, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.config import settings

from .base import Base


class GenericModel(Base):
    __abstract__ = True

    name: Mapped[str] = mapped_column(String(settings.name_max_len))

    def __repr__(self) -> str:
        return f"\nid: {self.id}" f"\nname: {self.name}\n"


class Vacancy(GenericModel):
    specialization_id: Mapped[int] = mapped_column(ForeignKey("specialization.id"))
    city_id: Mapped[int] = mapped_column(ForeignKey("city.id"))
    salary_from: Mapped[Decimal]
    salary_to: Mapped[Decimal]
    hr_salary: Mapped[Decimal]
    hr_salary_model: Mapped[int]
    employee_to_search: Mapped[int]
    number_of_recruiters: Mapped[int]
    #
    grade: Mapped[str] = mapped_column(String(settings.grade_max_len))
    experience: Mapped[str] = mapped_column(String(settings.experience_max_len))
    employment: Mapped[str] = mapped_column(String(settings.employment_max_len))
    registration_type: Mapped[str] = mapped_column(String(settings.reg_type_max_len))
    when_work: Mapped[str] = mapped_column(String(settings.when_work_max_len))
    what_need: Mapped[str] = mapped_column(String(settings.what_need_max_len))
    #
    work_types: Mapped[list] = mapped_column(ARRAY(String))
    responsibilities_ids = mapped_column(ARRAY(Integer))
    responsibilities_description: Mapped[str] = mapped_column(
        String(settings.description_max_len)
    )
    requirements_ids = mapped_column(ARRAY(Integer))
    requirements_description: Mapped[str] = mapped_column(
        String(settings.description_max_len)
    )
    conditions_ids = mapped_column(ARRAY(Integer))
    conditions_description: Mapped[str] = mapped_column(
        String(settings.description_max_len)
    )
    additional_tasks = mapped_column(ARRAY(String))
    special_requirements: Mapped[str] = mapped_column(
        String(settings.requirements_max_len), default=""
    )
    show_info: Mapped[bool] = mapped_column(Boolean, default=False)

    def __repr__(self) -> str:
        return (
            f"\nid: {self.id}"
            f"\nname: {self.name}"
            f"\nspecialization_id: {self.specialization_id}"
            f"\nsalary_from: {self.salary_from}"
            f"\nsalary_to: {self.salary_to}"
            f"\ngrade: {self.grade}"
            f"\nexperience: {self.experience}"
            f"\ncity_id: {self.city_id}"
            f"\nwork_type: {self.work_types}"
            f"\nemployment: {self.employment}"
            f"\nregistration_type: {self.registration_type}"
            f"\nresponsibilities: {self.responsibilities_ids}"
            f"\nresponsibilities_description: {self.responsibilities_description}"
            f"\nrequirements: {self.requirements_ids}"
            f"\nrequirements_description: {self.requirements_description}"
            f"\nconditions: {self.conditions_ids}"
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


class Condition(GenericModel):
    pass


class Category(GenericModel):
    specializations: Mapped[list["Specialization"]] = relationship(
        back_populates="category", cascade="all, delete-orphan", lazy="selectin"
    )


class Specialization(GenericModel):
    category_id: Mapped[int] = mapped_column(ForeignKey("category.id"))
    category: Mapped["Category"] = relationship(back_populates="specializations")

    responsibilities: Mapped[list["Responsibility"]] = relationship(
        back_populates="specialization", cascade="all, delete-orphan", lazy="selectin"
    )
    requirements: Mapped[list["Requirement"]] = relationship(
        back_populates="specialization", cascade="all, delete-orphan", lazy="selectin"
    )


class Responsibility(GenericModel):
    specialization_id: Mapped[int] = mapped_column(ForeignKey("specialization.id"))
    specialization: Mapped["Specialization"] = relationship(
        back_populates="responsibilities"
    )


class Requirement(GenericModel):
    specialization_id: Mapped[int] = mapped_column(ForeignKey("specialization.id"))
    specialization: Mapped["Specialization"] = relationship(
        back_populates="requirements"
    )
