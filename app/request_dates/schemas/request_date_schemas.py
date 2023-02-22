from datetime import date

from pydantic import BaseModel, UUID4
from enum import Enum
from typing import Optional


class RequestDateStatus(str, Enum):
    pending = "PENDING"
    approved = "APPROVED"
    denied = "DENIED"


class RequestDateSchema(BaseModel):
    id: UUID4
    request_id: str
    employee_id: str
    status: RequestDateStatus
    r_date: date

    class Config:
        orm_mode = True


class RequestDateSchemaIn(BaseModel):
    request_id: Optional[str]
    employee_id: Optional[str]
    status: Optional[RequestDateStatus]
    r_date: Optional[date]

    class Config:
        orm_mode = True


class EmployeeRequestDateSchema(BaseModel):
    request_id: str
    employee_id: str
    r_date: date

    class Config:
        orm_mode = True


class SuperiorRequestDateSchema(BaseModel):
    request_id: str
    status: RequestDateStatus

    class Config:
        orm_mode = True
