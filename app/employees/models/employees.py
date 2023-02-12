from datetime import datetime
from uuid import uuid4

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

    superior_id = Column(String(50), ForeignKey("employees.id"), nullable=True)
    holiday_group_id = Column(String(50), ForeignKey("holiday_groups.id"), nullable=True)
    superior = relationship("Employee", lazy="subquery")
    holiday_group = relationship("HolidayGroup", lazy="subquery")

    def __init__(self, email, password, first_name, last_name, date_of_birth,
                 phone_number, street_name, city, postal_code, country, days_off):
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
        self.days_off = days_off

