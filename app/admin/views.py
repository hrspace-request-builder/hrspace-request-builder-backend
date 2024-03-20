from starlette_admin.contrib.sqla import ModelView

from app.models.models import Vacancy


class VacancyView(ModelView):
    model = Vacancy
    fields = ("id", "name")
