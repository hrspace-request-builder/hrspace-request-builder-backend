from typing import Any

from pydantic import BaseModel


def get_400(name: str) -> dict[int, dict[str, Any]]:
    class Message(BaseModel):
        detail: str = f"{name} already exists"

    return {400: {"model": Message, "description": "The item already exists"}}


def get_404(name: str) -> dict[int, dict[str, Any]]:
    class Message(BaseModel):
        detail: str = f"{name} not found"

    return {404: {"model": Message, "description": "The item was not found"}}
