from fastapi import APIRouter

from app.core.business_logic import get_salary
from app.core.config import settings
from app.core.dependencies import async_session
from app.models import models
from app.repositories import crud
from app.schemas import schemas

from . import responses

SUM_CITIES = "Города России"
SUM_CATEGORIES = "Сферы деятельности (и их профессии)"
SUM_CONDITIONS = "Условия труда"
SUM_SPECIALIZATION = "Выбранная специализация (полный формат)"
SUM_SPECIALIZATIONS = "Список профессий (сокращенный формат)"
SUM_REQUIREMENTS = "Общий список требований"
SUM_RESPONSIBILITIES = "Общий список обязанностей"
SUM_ALL_VACANCY_NAMES = "Предлагаемые названия вакансий"
SUM_VACANCY_NAME_DATA = "Данные для полей заявки"
SUM_VACANCY = "Данные заполненной заявки"

router = APIRouter(prefix=f"{settings.URL_PREFIX}hrspace", tags=["First_page"])


@router.get(
    "/cities",
    response_model=list[schemas.CityOut],
    summary=SUM_CITIES,
    description=(f"{settings.ALL_USERS} {SUM_CITIES}"),
)
async def get_all_cities(session: async_session):
    return await crud.get_all(session, models.City)


@router.get(
    "/vacancy_names",
    response_model=list[schemas.ShortSpecialization],
    summary=SUM_ALL_VACANCY_NAMES,
    description=(f"{settings.ALL_USERS} {SUM_ALL_VACANCY_NAMES}"),
)
async def get_all_vacancies(session: async_session) -> list:
    return await crud.get_all(session, models.Specialization)


@router.get(
    "/categories",
    response_model=list[schemas.CategoryOut],
    summary=SUM_CATEGORIES,
    description=(f"{settings.ALL_USERS} {SUM_CATEGORIES}"),
)
async def get_all_categories(session: async_session):
    return await crud.get_all(session, models.Category)


@router.get(
    "/specializations/{vacancy_name_id}",
    response_model=schemas.FullSpecialization,
    responses={**responses.get_404("Specialization")},
    summary=SUM_SPECIALIZATION,
    description=(f"{settings.ALL_USERS} {SUM_SPECIALIZATION}"),
)
async def get_spec(vacancy_name_id: int, session: async_session):
    return await crud.get_or_404(session, models.Specialization, vacancy_name_id)


@router.get(
    "/data/",
    responses={**responses.get_404("City or specialization")},
    summary=SUM_VACANCY_NAME_DATA,
    description=(f"{settings.ALL_USERS} {SUM_VACANCY_NAME_DATA}"),
)
async def get_data(vacancy_name_id: int, city_id: int, session: async_session):
    spec = await crud.get_or_404(session, models.Specialization, vacancy_name_id)
    salary = await get_salary(session, city_id)
    conditions = [c.asdict() for c in await crud.get_all(session, models.Condition)]
    return {**spec.__dict__, **{"salary": salary, "conditions": conditions}}


@router.post(
    "/vacancy",
    status_code=201,
    # response_model=schemas.VacancyOut,
    # responses={**responses.get_400("Object")},
    summary=SUM_VACANCY,
    description=(f"{settings.ALL_USERS} {SUM_VACANCY}"),
)
async def post_vacancy(payload: schemas.VacancyIn, session: async_session):
    pass
