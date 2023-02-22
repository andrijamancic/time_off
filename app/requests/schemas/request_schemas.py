from datetime import date

from pydantic import BaseModel, UUID4, StrictBool
from enum import Enum
from typing import Optional


class RequestType(str, Enum):
    pto = 'PTO'
    sick = 'SICK'
    unpaid = 'UNPAID'


class RequestSchema(BaseModel):
    id: UUID4
    employee_id: UUID4
    type: RequestType
    message: str
    superior_message: str
    cancelled: StrictBool = False
    request_date: date
    response_date: date

    class Config:
        orm_mode = True


class RequestSchemaIn(BaseModel):
    employee_id: UUID4
    type: RequestType
    message: Optional[str]
    superior_message: Optional[str]
    cancelled: Optional[StrictBool] = False
    request_date: Optional[date]
    response_date: Optional[date]

    class Config:
        orm_mode = True


class RequestSchemaEmployee(BaseModel):
    employee_id: UUID4
    type: RequestType
    message: Optional[str]
    request_date: Optional[date]
    response_date: Optional[date]

    class Config:
        orm_mode = True
