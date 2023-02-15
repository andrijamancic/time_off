from uuid import uuid4
from sqlalchemy import Column, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from app.db import Base


class HolidayGroupDate(Base):
    __tablename__ = "holiday_group_dates"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    name = Column(String(250), nullable=False, unique=True)
    date = Column(Date)

    holiday_group_id = Column(String(50), ForeignKey("holiday_groups.id"), nullable=True)
    request = relationship("HolidayGroup", lazy="subquery")

    def __init__(self, name: str, date: date, holiday_group_id: str):
        self.name = name
        self.date = date
        self.holiday_group_id = holiday_group_id
