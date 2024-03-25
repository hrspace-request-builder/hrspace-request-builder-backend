from decimal import Decimal

from sqlalchemy.ext.asyncio import AsyncSession

from app.models.models import City
from app.repositories import crud


async def get_salary(session: AsyncSession, city_id: int) -> dict[str, Decimal]:
    city = await crud.get_or_404(session, City, city_id)  # noqa
    # TODO: calculate salary min/max as per city
    return {"min": Decimal(1000.00), "max": Decimal(2000.00)}
