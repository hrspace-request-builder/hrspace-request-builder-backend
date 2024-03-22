from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.config import settings

from .base import Base


class GenericModel(Base):
    __abstract__ = True

    name: Mapped[str] = mapped_column(String(settings.name_max_len))
    #    String(settings.name_max_len), unique=True, index=True)

    def __repr__(self) -> str:
        return f"\nid: {self.id}" f"\nname: {self.name}\n"


class VacancyName(GenericModel):
    pass


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
