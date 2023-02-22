from fastapi import APIRouter, Depends

from app.employees.controller.employee_auth_controller import JWTBearer
from app.holiday_groups.controller.holiday_group_controller import HolidayGroupController

from app.holiday_groups.schemas import HolidayGroupSchema, HolidayGroupSchemaIn


holiday_group_router = APIRouter(tags=["holiday-groups"], prefix="/api/holiday-groups")


@holiday_group_router.post("/add-new-holiday-group", response_model=HolidayGroupSchema,
                           dependencies=[Depends(JWTBearer("superior_employee"))])
def create_holiday_group(holiday_date: HolidayGroupSchemaIn):
    return HolidayGroupController.create_holiday_group(holiday_date.name)


@holiday_group_router.get("/get-all-holiday-groups", response_model=list[HolidayGroupSchema])
def get_all_holiday_groups():
    return HolidayGroupController.get_all_holiday_groups()


@holiday_group_router.get("/id", response_model=HolidayGroupSchema)
def get_holiday_group_by_id(holiday_group_id: str):
    return HolidayGroupController.get_holiday_group_by_id(holiday_group_id)


@holiday_group_router.delete("/", dependencies=[Depends(JWTBearer("superior_employee"))])
def delete_holiday_group_by_id(holiday_group_id: str):
    return HolidayGroupController.delete_holiday_group_by_id(holiday_group_id)


@holiday_group_router.put("/update", response_model=HolidayGroupSchema,
                          dependencies=[Depends(JWTBearer("superior_employee"))])
def update_holiday_group_by_id(holiday_group_id, name: str = None):
    return HolidayGroupController.update_holiday_group(holiday_group_id, name)
