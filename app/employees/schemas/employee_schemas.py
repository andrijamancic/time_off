from datetime import date

from pydantic import BaseModel
from pydantic import UUID4


class EmployeeSchema(BaseModel):
    id: UUID4
    email: str
    password: str
    first_name: str
    last_name: str
    date_of_birth: date
    phone_number: str
    street_name: str
    city: str
    postal_code: str
    country: str
    superior_id: str
    holiday_group_id: str
    days_off: int

    class Config:
        orm_mode = True


class EmployeeSchemaIn(BaseModel):
    email: str
    password: str
    first_name: str
    last_name: str
    date_of_birth: date
    phone_number: str
    street_name: str
    city: str
    postal_code: str
    country: str
    superior_id: str
    holiday_group_id: str
    days_off: int

    class Config:
        orm_mode = True
