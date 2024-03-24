from starlette_admin.contrib.sqla import Admin
from app.core.dependencies import engine
from .views import City, CityView

admin = Admin(
    engine,
    "💾 База данных HRSpace",
)

admin.add_view(CityView(City))
# admin.add_view(VacancyView(VacancyName))
