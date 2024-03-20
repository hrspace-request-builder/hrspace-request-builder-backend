from fastapi import APIRouter

from app.core.config import settings
from app.core.dependencies import async_session
from app.models.models import Vacancy
from app.schemas import schemas

SUM_ALL_VACANCY_NAMES = "ALL_VACANCY_NAMES"
SUM_VACANCY_NAME_DATA = "Data for particular vacancy name"

router = APIRouter(prefix=f"{settings.URL_PREFIX}first_page", tags=["First_page"])


@router.get(
    "/vacancy_names",
    response_model=list[schemas.VacancyNamesOut],
    summary=SUM_ALL_VACANCY_NAMES,
    description=(f"{settings.ALL_USERS} {SUM_ALL_VACANCY_NAMES}"),
)
async def get_all_vacancies(session: async_session) -> list:
    from sqlalchemy import select

    stmt = select(Vacancy)
    return await session.scalars(stmt)


@router.get(
    "/data/",
    # response_model=list[schemas.VacancyNamesOut],
    summary=SUM_ALL_VACANCY_NAMES,
    description=(f"{settings.ALL_USERS} {SUM_ALL_VACANCY_NAMES}"),
)
async def read_data(vacancy_name_id: int = 0):
    return None
