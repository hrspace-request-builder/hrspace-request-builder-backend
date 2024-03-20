from fastapi import APIRouter

from app.core.config import settings
from app.core.dependencies import async_session
from app.models.models import City, Vacancy
from app.schemas import schemas

SUM_ALL_VACANCY_NAMES = "Names of all vacancies"
SUM_VACANCY_NAME_DATA = "Data for particular vacancy name"
SUM_CITIES = "All cities"

router = APIRouter(prefix=f"{settings.URL_PREFIX}first_page", tags=["First_page"])


async def get_all(session, model):
    """Brief crud."""
    from sqlalchemy import select

    stmt = select(model)
    return await session.scalars(stmt)


@router.get(
    "/vacancy_names",
    response_model=list[schemas.VacancyNamesOut],
    summary=SUM_ALL_VACANCY_NAMES,
    description=(f"{settings.ALL_USERS} {SUM_ALL_VACANCY_NAMES}"),
)
async def get_all_vacancies(session: async_session) -> list:
    return await get_all(session, Vacancy)


@router.get(
    "/cities",
    response_model=list[schemas.CityOut],
    summary=SUM_CITIES,
    description=(f"{settings.ALL_USERS} {SUM_CITIES}"),
)
async def get_all_cities(session: async_session):
    return await get_all(session, City)


@router.get(
    "/data/",
    response_model=schemas.Data,
    summary=SUM_VACANCY_NAME_DATA,
    description=(f"{settings.ALL_USERS} {SUM_VACANCY_NAME_DATA}"),
)
async def get_data(vacancy_name_id: int = 0):
    return None
