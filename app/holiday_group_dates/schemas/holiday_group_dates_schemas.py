from datetime import date

from pydantic import BaseModel, UUID4, StrictStr


class HolidayGroupDateSchema(BaseModel):
    id: UUID4
    holiday_group_id: str
    date: date
    name: StrictStr

    class Config:
        orm_mode = True


class HolidayGroupDateSchemaIn(BaseModel):
    holiday_group_id: str
    date: date
    name: StrictStr

    class Config:
        orm_mode = True
