from fastapi import APIRouter

from app import schemas  # noqa
from app.core.config import settings
from .responses import get_400, get_404

SUM_ALL_ITEMS = "ALL_ITEMS"

router = APIRouter(prefix=f"{settings.URL_PREFIX}items", tags=["Items"])


@router.get(
    "",
    # response_model=list[schemas.],
    responses={**get_400("Item"), **get_404("Item")},
    summary=SUM_ALL_ITEMS,
    description=(f"{settings.ALL_USERS} {SUM_ALL_ITEMS}"),
)
async def get_all_items() -> list:
    return ["ALL", "ITEMS"]
