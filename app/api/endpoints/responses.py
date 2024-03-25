from typing import Any

from pydantic import BaseModel


def get_400(name: str) -> dict[int, dict[str, Any]]:
    bad_request_msg = "already exists"

    class Message(BaseModel):
        detail: str = f"{name} {bad_request_msg}"

    return {400: {"model": Message, "description": f"The item {bad_request_msg}"}}


def get_404(name: str) -> dict[int, dict[str, Any]]:
    not_found_msg = "was not found"

    class Message(BaseModel):
        detail: str = f"{name} {not_found_msg}"

    return {404: {"model": Message, f"{not_found_msg}": ""}}
