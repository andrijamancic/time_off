from uuid import uuid4
from datetime import date
from sqlalchemy import Column, String, ForeignKey, Date, Integer
from sqlalchemy.orm import relationship

from app.db import Base


class Employee(Base):
    __tablename__ = "employees"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    email = Column(String(100), unique=True)
    password = Column(String(100))
    first_name = Column(String(100))
    last_name = Column(String(100))
    date_of_birth = Column(Date)
    phone_number = Column(String(30))
    street_name = Column(String(30))
    city = Column(String(30))
    postal_code = Column(String(30))
    country = Column(String(30))
    days_off = Column(Integer)

    holiday_group_id = Column(String(50), ForeignKey("holiday_groups.id"), nullable=True)
    superior_id = Column(String(50), ForeignKey("employees.id"), default=None)
    superior = relationship("Employee", lazy="subquery")
    holiday_group = relationship("HolidayGroup", lazy="subquery")

    def __init__(self, email: str, password: str, first_name: str, last_name: str, date_of_birth: date,
                 phone_number: str, street_name: str, city: str, postal_code: str, country: str,
                 holiday_group_id: str, superior_id: str, days_off: int):
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.phone_number = phone_number
        self.street_name = street_name
        self.city = city
        self.postal_code = postal_code
        self.country = country
        self.holiday_group_id = holiday_group_id
        self.superior_id = superior_id
        self.days_off = days_off
