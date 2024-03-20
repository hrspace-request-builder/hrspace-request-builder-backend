from sqlalchemy import String
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
    pass


class City(GenericModel):
    pass
