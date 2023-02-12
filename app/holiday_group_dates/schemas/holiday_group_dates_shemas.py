from datetime import date

from pydantic import BaseModel, UUID4


class HolidayGroupDateSchema(BaseModel):
    id: UUID4
    holiday_group_id: str
    date: date
    name: str

    class Config:
        orm_mode = True


class HolidayGroupDateSchemaIn(BaseModel):
    holiday_group_id: str
    date: date
    name: str

    class Config:
        orm_mode = True
