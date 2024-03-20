from starlette_admin.contrib.sqla import ModelView

from app.models.models import City, Vacancy


class GenericView(ModelView):
    fields = ("id", "name")


class CityView(GenericView):
    model = City
    name = "Города"


class VacancyView(GenericView):
    model = Vacancy
    name = "Названия вакансий"
