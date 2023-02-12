from uuid import uuid4

from sqlalchemy import Column, String, DATE, ForeignKey, Enum
from sqlalchemy.orm import relationship

from app.db import Base


class RequestStatus(Enum):
    approved = 1
    denied = 2


class RequestDate(Base):
    __tablename__ = "request_dates"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    date = Column(DATE)
    status = Column(RequestStatus)

    request_id = Column(String(50), ForeignKey("requests.id"), nullable=False)
    employee_id = Column(String(50), ForeignKey("employees.id"), nullable=False)

    request = relationship("Request", lazy="subquery")
    employee = relationship("Employee", lazy="subquery")

    def __init__(self, date: date):
        self.date = date

