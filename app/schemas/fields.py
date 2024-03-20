from typing import Any

from pydantic import Field

from app.core.config import settings


def name_field(*args) -> Any:
    return Field(max_length=settings.name_max_len, examples=args)
