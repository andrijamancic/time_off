from datetime import date
from app.db.database import SessionLocal
from app.holiday_group_dates.repositories.holiday_group_date_repository import HolidayGroupDateRepository


class HolidayGroupDateServices:
    @staticmethod
    def create_holiday_group_date(name: str, date: date, holiday_group_id: str):
        try:
            with SessionLocal() as db:
                holiday_group_date_repository = HolidayGroupDateRepository(db)
                return holiday_group_date_repository.create_holiday_group_date(name, date, holiday_group_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_all_holiday_dates():
        try:
            with SessionLocal() as db:
                holiday_group_date_repository = HolidayGroupDateRepository(db)
                return holiday_group_date_repository.get_all_holiday_dates()
        except Exception as e:
            raise e

    @staticmethod
    def get_holiday_group_date_by_id(holiday_group_date_id: str):
        try:
            with SessionLocal() as db:
                holiday_group_date_repository = HolidayGroupDateRepository(db)
                return holiday_group_date_repository.get_holiday_group_date_by_id(holiday_group_date_id)
        except Exception as e:
            raise e

    @staticmethod
    def delete_holiday_group_date_by_id(holiday_group_date_id: str):
        try:
            with SessionLocal() as db:
                holiday_group_repository = HolidayGroupDateRepository(db)
                holiday_group_repository.delete_holiday_group_date_by_id(holiday_group_date_id)
                return True
        except Exception as e:
            raise e

    @staticmethod
    def update_holiday_group_date_by_id(holiday_group_date_id: str,
                                        name: str = None,
                                        date: date = None,
                                        holiday_group_id: str = None):
        try:
            with SessionLocal() as db:
                holiday_group = HolidayGroupDateRepository(db)
                return holiday_group.update_holiday_group_date_by_id(holiday_group_date_id, name,
                                                                     date, holiday_group_id)
        except Exception as e:
            raise e
