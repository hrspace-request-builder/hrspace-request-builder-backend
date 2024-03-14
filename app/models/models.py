from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Vacancy(Base):
    title: Mapped[str] = mapped_column(String(256), unique=True, index=True)
    description: Mapped[str] = mapped_column(String(2000), unique=True, index=True)

    def __repr__(self) -> str:
        return (
            f"\nid: {self.id}"
            f"\ntitle: {self.title}"
            f"\ndescription: {self.description}\n"
        )
