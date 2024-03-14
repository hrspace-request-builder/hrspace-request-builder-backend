"""
from pydantic import BaseModel, ConfigDict, Field, field_validator

# constants for examples



class IdMixin(BaseModel):
    id: str
    model_config = ConfigDict(from_attributes=True)
"""
