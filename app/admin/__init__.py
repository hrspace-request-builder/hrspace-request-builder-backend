from starlette_admin.contrib.sqla import Admin
from app.core.dependencies import engine
from app.models import models as m
from . import views as v

admin = Admin(
    engine,
    "💾 База данных HRSpace",
)

admin.add_view(v.VacancyView(m.Vacancy))
admin.add_view(v.CategoryView(m.Category))
admin.add_view(v.CityView(m.City))
admin.add_view(v.ConditionView(m.Condition))
admin.add_view(v.RequirementsView(m.Requirement))
admin.add_view(v.ResponsibilitiesView(m.Responsibility))
admin.add_view(v.SpecializationView(m.Specialization))
