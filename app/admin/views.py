from starlette_admin.contrib.sqla import ModelView

from app.models.models import City, Specialization, Vacancy


class GenericView(ModelView):
    fields = ("id", "name")


class CityView(GenericView):
    model = City
    name = "Города"


class SpecializationView(GenericView):
    model = Specialization
    name = "Специальность"


class VacancyView(ModelView):
    # fields = "__all__"
    model = Vacancy
    name = "Заявка"
