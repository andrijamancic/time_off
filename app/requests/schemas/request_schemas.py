from datetime import datetime

from pydantic import BaseModel, UUID4
from enum import Enum


class RequestSchema(BaseModel):
    id: UUID4
    employee_id: UUID4
    type: Enum
    message: str
    superior_message: str
    cancelled: Enum
    request_date: datetime
    response_date: datetime

    class Config:
        orm_mode = True


class RequestSchemaIn(BaseModel):
    employee_id: UUID4
    type: Enum
    message: str
    superior_message: str
    cancelled: Enum
    request_date: datetime
    response_date: datetime

    class Config:
        orm_mode = True
