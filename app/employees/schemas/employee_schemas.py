from datetime import date

from pydantic import BaseModel, UUID4, EmailStr
from typing import Optional


class EmployeeSchema(BaseModel):
    id: UUID4
    email: EmailStr
    password: str
    first_name: str
    last_name: str
    date_of_birth: date
    phone_number: str
    street_name: str
    city: str
    postal_code: str
    country: str
    holiday_group_id: str
    superior_id: Optional[str]
    days_off: int

    class Config:
        orm_mode = True


class EmployeeSchemaIn(BaseModel):
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    date_of_birth: Optional[date] = None
    phone_number: Optional[str] = None
    street_name: Optional[str] = None
    city: Optional[str] = None
    postal_code: Optional[str] = None
    country: Optional[str] = None
    holiday_group_id: str
    superior_id: Optional[str] = None
    days_off: Optional[int] = None

    class Config:
        orm_mode = True


class EmployeeLoginSchema(BaseModel):
    email: EmailStr
    password: str
