

from app.db.database import SessionLocal
from app.holiday_groups.repositories.holiday_group_repository import HolidayGroupRepository


class HolidayGroupServices:
    @staticmethod
    def create_holiday_group(name: str):
        try:
            with SessionLocal() as db:
                holiday_group_date_repository = HolidayGroupRepository(db)
                return holiday_group_date_repository.create_holiday_group(name)
        except Exception as e:
            raise e

    @staticmethod
    def get_all_holiday_groups():
        try:
            with SessionLocal() as db:
                holiday_group_repository = HolidayGroupRepository(db)
                return holiday_group_repository.get_all_holiday_groups()
        except Exception as e:
            raise e

    @staticmethod
    def get_holiday_group_by_id(holiday_group_id: str):
        try:
            with SessionLocal() as db:
                holiday_group_repository = HolidayGroupRepository(db)
                return holiday_group_repository.get_holiday_group_by_id(holiday_group_id)
        except Exception as e:
            raise e

    @staticmethod
    def delete_holiday_group_by_id(holiday_group_id: str):
        try:
            with SessionLocal() as db:
                holiday_group_repository = HolidayGroupRepository(db)
                holiday_group_repository.delete_holiday_group_by_id(holiday_group_id)
                return True
        except Exception as e:
            raise e

    @staticmethod
    def update_holiday_group(holiday_group_id: str, name: str = None):
        try:
            with SessionLocal() as db:
                holiday_group = HolidayGroupRepository(db)
                return holiday_group.update_holiday_group(holiday_group_id, name)
        except Exception as e:
            raise e
