from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


async def get(session: AsyncSession, model, exception: bool = False, **kwargs):
    stmt = select(model).filter_by(**kwargs)
    result = await session.scalars(stmt)
    res = result.all() if kwargs.get("id") is None else result.first()
    if not res and exception:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Объект не найден")
    return res


async def get_all(session: AsyncSession, model):
    return await get(session, model)


async def get_or_404(session: AsyncSession, model, id: int):
    return await get(session, model, exception=True, id=id)


async def create(session: AsyncSession, model, **kwargs):
    obj = model(**kwargs)
    session.add(obj)
    await session.commit()
    await session.refresh(obj)
    return obj
