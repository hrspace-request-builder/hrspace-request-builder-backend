import csv

from sqlalchemy import insert

from app.core.dependencies import AsyncSessionLocal
from app.models import models as m

DATA = (
    (m.City, "app/data/cities.csv"),
    (m.Condition, "app/data/conditions.csv"),
    (m.Category, "app/data/categories.csv"),
    (m.Specialization, "app/data/specializations.csv"),
    (m.Requirement, "app/data/requirements.csv"),
    (m.Responsibility, "app/data/responsibilities.csv"),
)


def read_csvfile(file_name: str) -> list[dict[str, str | int]]:
    with open(file_name, newline="") as f:
        return [row for row in csv.DictReader(f)]


def convert_to_int(rows: list[dict[str, str | int]]) -> None:
    for row in rows:
        for key in row:
            try:
                row[key] = int(row[key])
            except (TypeError, ValueError):
                pass


async def load_csv(model, file_name: str) -> None:
    rows = read_csvfile(file_name)
    convert_to_int(rows)
    async with AsyncSessionLocal.begin() as session:
        await session.execute(insert(model), rows)


async def load_models_data():
    for model, scv_file in DATA:
        await load_csv(model, scv_file)
