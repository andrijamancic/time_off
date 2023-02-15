from datetime import date
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.holiday_group_dates.exceptions import HolidayGroupDateNotFoundException
from app.holiday_group_dates.models import HolidayGroupDate


class HolidayGroupDateRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_holiday_group_date(self, name: str, date: date, holiday_group_id: str):
        try:
            holiday_group_date = HolidayGroupDate(name, date, holiday_group_id)
            self.db.add(holiday_group_date)
            self.db.commit()
            self.db.refresh(holiday_group_date)
            return holiday_group_date
        except IntegrityError as e:
            raise e

    def get_all_holiday_dates(self):
        holiday_group_date = self.db.query(HolidayGroupDate).all()
        return holiday_group_date

    def get_holiday_group_date_by_id(self, holiday_group_date_id: str):
        holiday_group_date = self.db.query(HolidayGroupDate).filter(HolidayGroupDate.id == holiday_group_date_id).first()
        if holiday_group_date is None:
            raise HolidayGroupDateNotFoundException(f"Holiday group with ID: {holiday_group_date_id} not found.", 400)
        return holiday_group_date

    def delete_holiday_group_date_by_id(self, holiday_group_date_id: str):
        try:
            holiday_group_date = self.db.query(HolidayGroupDate).filter(HolidayGroupDate.id == holiday_group_date_id).first()
            if holiday_group_date is None:
                raise HolidayGroupDateNotFoundException(
                    f"Holiday group with ID: {holiday_group_date_id} not found.", 400,)
            self.db.delete(holiday_group_date)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update_holiday_group_date_by_id(self, holiday_group_date_id: str, name: str = None, date: date = None,
                                        holiday_group_id: str = None):
        try:
            holiday_group_date = self.db.query(HolidayGroupDate).filter(HolidayGroupDate.id == holiday_group_date_id).first()
            if holiday_group_date is None:
                raise HolidayGroupDateNotFoundException(f"Holiday group date with ID: {holiday_group_date_id}  not found.", 400)
            if name is not None:
                holiday_group_date.name = name
            if date is not None:
                holiday_group_date.date = date
            if holiday_group_id is not None:
                holiday_group_date.holiday_group_id = holiday_group_id
            self.db.add(holiday_group_date)
            self.db.commit()
            self.db.refresh(holiday_group_date)
            return holiday_group_date
        except Exception as e:
            raise e
