from datetime import date
from fastapi import HTTPException, Response, status

from app.holiday_group_dates.exceptions import HolidayGroupDateNotFoundException
from app.holiday_group_dates.services.holiday_group_dates_services import HolidayGroupDateServices


class HolidayGroupDateController:
    @staticmethod
    def create_holiday_group_date(name: str, date: date, holiday_group_id: str):
        try:
            holiday_group_date = HolidayGroupDateServices.create_holiday_group_date(name, date, holiday_group_id)
            return holiday_group_date
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_holiday_dates():
        try:
            holiday_group_date = HolidayGroupDateServices.get_all_holiday_dates()
            return holiday_group_date
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_holiday_group_date_by_id(holiday_group_date_id: str):
        try:
            holiday_group_date = HolidayGroupDateServices.get_holiday_group_date_by_id(holiday_group_date_id)
            if holiday_group_date:
                return holiday_group_date
        except HolidayGroupDateNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_holiday_group_date_by_id(holiday_group_date_id: str):
        try:
            HolidayGroupDateServices.delete_holiday_group_date_by_id(holiday_group_date_id)
            return Response(content=f"Holiday date with id - {holiday_group_date_id} deleted successfully")
        except HolidayGroupDateNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def update_holiday_group_date_by_id(holiday_group_date_id: str,
                                        name: str = None,
                                        date: date = None,
                                        holiday_group_id: str = None
                                        ):
        try:
            holiday_group_date = HolidayGroupDateServices.update_holiday_group_date_by_id(holiday_group_date_id, name,
                                                                                          date, holiday_group_id)
            return holiday_group_date
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))