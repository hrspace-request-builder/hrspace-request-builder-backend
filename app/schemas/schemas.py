from pydantic import BaseModel, ConfigDict, Field

# constants for examples
VACANCY_NAME = "Vacancy name"
DESCRIPTION = "My vacancy description"


"""class VacancyOut(BaseModel):
    id: int
    title: str = Field(max_length=256, examples=[TITLE])
    description: str = Field(max_length=2000, examples=[DESCRIPTION])
    model_config = ConfigDict(arbitrary_types_allowed=True, from_attributes=True)"""


class VacancyNamesOut(BaseModel):
    id: int
    name: str = Field(max_length=256, examples=[VACANCY_NAME])
    model_config = ConfigDict(arbitrary_types_allowed=True, from_attributes=True)
