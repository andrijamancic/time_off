from fastapi import APIRouter, Depends

from app.employees.controller.employee_auth_controller import JWTBearer
from app.holiday_group_dates.controller.holiday_group_date_controller import HolidayGroupDateController

from app.holiday_group_dates.schemas import HolidayGroupDateSchema, HolidayGroupDateSchemaIn


holiday_group_dates_router = APIRouter(tags=["holiday-dates"], prefix="/api/holiday-days")


@holiday_group_dates_router.post("/add-new-holiday-date", response_model=HolidayGroupDateSchema,
                                 dependencies=[Depends(JWTBearer("superior_employee"))])
def create_holiday_date(holiday_date: HolidayGroupDateSchemaIn):
    return HolidayGroupDateController.create_holiday_group_date(holiday_date.name, holiday_date.date,
                                                                holiday_date.holiday_group_id)


@holiday_group_dates_router.get("/get-all-holiday-dates", response_model=list[HolidayGroupDateSchema])
def get_all_holiday_dates():
    return HolidayGroupDateController.get_all_holiday_dates()


@holiday_group_dates_router.get("/id", response_model=HolidayGroupDateSchema)
def get_holiday_date_by_id(holiday_group_date_id: str):
    return HolidayGroupDateController.get_holiday_group_date_by_id(holiday_group_date_id)


@holiday_group_dates_router.delete("/", dependencies=[Depends(JWTBearer("superior_employee"))])
def delete_holiday_group_date_by_id(holiday_group_date_id: str):
    return HolidayGroupDateController.delete_holiday_group_date_by_id(holiday_group_date_id)


@holiday_group_dates_router.put("/update", response_model=HolidayGroupDateSchema,
                                dependencies=[Depends(JWTBearer("superior_employee"))])
def update_holiday_group_date_by_id(holiday_group_date_id, name: str = None):
    return HolidayGroupDateController.update_holiday_group_date_by_id(holiday_group_date_id, name)