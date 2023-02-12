from pydantic import BaseModel, UUID4


class HolidayGroupSchema(BaseModel):
    id: UUID4
    name: str

    class Config:
        orm_mode = True


class HolidayGroupSchemaIn(BaseModel):
    name: str

    class Config:
        orm_mode = True
