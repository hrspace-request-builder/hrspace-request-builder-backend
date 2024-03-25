from starlette_admin.contrib.sqla import ModelView

from app.models import models as m


class CityView(ModelView):
    model = m.City
    name = "Города"


class SpecializationView(ModelView):
    model = m.Specialization
    name = "Специальность"


class VacancyView(ModelView):
    model = m.Vacancy
    name = "Заявка"


class CategoryView(ModelView):
    model = m.Category
    name = "Сфера деятельности"


class ConditionView(ModelView):
    model = m.Condition
    name = "Условия труда"


class RequirementsView(ModelView):
    model = m.Requirement
    name = "Требования"


class ResponsibilitiesView(ModelView):
    model = m.Responsibility
    name = "Обязанности"
