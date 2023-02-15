from uuid import uuid4

from sqlalchemy import Column, String
from app.db import Base


class HolidayGroup(Base):
    __tablename__ = "holiday_groups"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    name = Column(String(250), nullable=False, unique=True)

    def __init__(self, name: str):
        self.name = name
