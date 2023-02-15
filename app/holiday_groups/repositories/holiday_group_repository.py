from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.holiday_groups.exceptions import HolidayGroupNotFoundException
from app.holiday_groups.models import HolidayGroup


class HolidayGroupRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_holiday_group(self, name: str):
        try:
            holiday_group = HolidayGroup(name)
            self.db.add(holiday_group)
            self.db.commit()
            self.db.refresh(holiday_group)
            return holiday_group
        except IntegrityError as e:
            raise e

    def get_all_holiday_groups(self):
        holiday_group = self.db.query(HolidayGroup).all()
        return holiday_group

    def get_holiday_group_by_id(self, holiday_group_id: str):
        holiday_group = self.db.query(HolidayGroup).filter(HolidayGroup.id == holiday_group_id).first()
        if holiday_group is None:
            raise HolidayGroupNotFoundException(f"Holiday group with ID: {holiday_group_id} not found.", 400)
        return holiday_group

    def delete_holiday_group_by_id(self, holiday_group_id: str):
        try:
            holiday_group = self.db.query(HolidayGroup).filter(HolidayGroup.id == holiday_group_id).first()
            if holiday_group is None:
                raise HolidayGroupNotFoundException(
                    f"Holiday group with ID: {holiday_group_id} not found.", 400,)
            self.db.delete(holiday_group)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update_holiday_group(self, holiday_group_id: str, name: str = None):
        try:
            holiday_group = self.db.query(HolidayGroup).filter(HolidayGroup.id == holiday_group_id).first()
            if holiday_group is None:
                raise HolidayGroupNotFoundException(f"Holiday group with ID: {holiday_group_id}  not found.", 400)
            if name is not None:
                holiday_group.name = name
            self.db.add(holiday_group)
            self.db.commit()
            self.db.refresh(holiday_group)
            return holiday_group
        except Exception as e:
            raise e
