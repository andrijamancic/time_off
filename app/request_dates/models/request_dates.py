from uuid import uuid4

from sqlalchemy import Column, String, Date, ForeignKey, Enum
from sqlalchemy.orm import relationship
from datetime import date

from app.db import Base
from app.request_dates.schemas import RequestDateStatus


class RequestDate(Base):
    __tablename__ = "request_dates"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    r_date = Column(Date)
    status = Column(Enum(RequestDateStatus))

    request_id = Column(String(50), ForeignKey("requests.id"), nullable=False)
    employee_id = Column(String(50), ForeignKey("employees.id"), nullable=False)

    request = relationship("Request", lazy="subquery")
    employee = relationship("Employee", lazy="subquery")

    def __init__(self, r_date: date, status: RequestDateStatus, request_id: str, employee_id: str):
        self.r_date = r_date
        self.status = status
        self.request_id = request_id
        self.employee_id = employee_id

