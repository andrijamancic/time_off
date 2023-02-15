from fastapi import HTTPException, Response, status
from sqlalchemy import Date

from app.employees.exceptions import *
from app.holiday_groups.exceptions import HolidayGroupNotFoundException
from app.holiday_groups.services.holiday_groups_services import HolidayGroupServices


class HolidayGroupController:
    @staticmethod
    def create_holiday_group(name: str):
        try:
            holiday_group = HolidayGroupServices.create_holiday_group(name)
            return holiday_group
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_holiday_groups():
        try:
            holiday_group = HolidayGroupServices.get_all_holiday_groups()
            return holiday_group
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_holiday_group_by_id(holiday_group_id: str):
        try:
            holiday_group = HolidayGroupServices.get_holiday_group_by_id(holiday_group_id)
            if holiday_group:
                return holiday_group
        except HolidayGroupNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_holiday_group_by_id(holiday_group_id: str):
        try:
            HolidayGroupServices.delete_holiday_group_by_id(holiday_group_id)
            return Response(content=f"Holiday group with id - {holiday_group_id} deleted successfully")
        except HolidayGroupNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def update_holiday_group(employee_id: str, name: str = None):
        try:
            employee = HolidayGroupServices.update_holiday_group(employee_id, name)
            return employee
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))