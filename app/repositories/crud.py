from fastapi import HTTPException, status
from sqlalchemy import insert, select
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
    return await session.execute(insert(model).values(**kwargs))


'''
    # obj = model(**kwargs)

    async def _save(self, obj: ModelType) -> ModelType:
        """Raises `BAD_REQUEST` exception if object already exists in DB. """
        self.session.add(obj)
        try:
            await self.session.commit()
        except exc.IntegrityError:
            await self.session.rollback()
            raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                self.msg_already_exists)
        await self.session.refresh(obj)
        return obj
'''
