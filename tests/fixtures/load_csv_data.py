from sqlalchemy import insert

from app.data.load_data import DATA, convert_to_int, read_csvfile  # noqa

from .db import TestingSessionLocal


async def load_csv(model, file_name: str) -> None:
    rows = read_csvfile(file_name)
    convert_to_int(rows)
    async with TestingSessionLocal.begin() as session:
        await session.execute(insert(model), rows)
