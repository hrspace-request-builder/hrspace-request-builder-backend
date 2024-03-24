from decimal import Decimal


# type: ignore [dict-item]
def get_salary(city_id: int) -> dict[str, Decimal]:
    # TODO: calculate salary min/max as per city
    # city = crud.get_or_404(session, City)
    return {"min": Decimal(1000.00), "max": Decimal(2000.00)}
