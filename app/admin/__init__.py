from starlette_admin.contrib.sqla import Admin
from .views import VacancyView, Vacancy
from app.core.dependencies import engine


admin = Admin(
    engine,
    "💾 База данных HRSpace",
)
admin.add_view(VacancyView(Vacancy))
