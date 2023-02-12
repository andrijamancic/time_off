from datetime import date

from pydantic import BaseModel, UUID4
from enum import Enum


class RequestDateSchema(BaseModel):
    id: UUID4
    request_id: str
    employee_id: str
    status: Enum
    date: date

    class Config:
        orm_mode = True


class RequestDateSchemaIn(BaseModel):
    request_id: str
    employee_id: str
    status: Enum
    date: date

    class Config:
        orm_mode = True
