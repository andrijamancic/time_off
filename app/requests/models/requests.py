from uuid import uuid4
from datetime import datetime

from sqlalchemy import Column, String, Date, ForeignKey, Enum
from app.db import Base


class RequestType(Enum):
    pto = 1
    sick = 2
    unpaid = 3


class CancelledType(Enum):
    true = 1
    false = 2


class Request(Base):
    __tablename__ = "requests"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    type = Column(RequestType)
    cancelled = Column(CancelledType)
    message = Column(String(250))
    superior_message = Column(String(250))
    request_date = Column(Date)
    response_date = Column(Date)

    employee_id = Column(String, ForeignKey("employees.id"), nullable=False)

    def __init__(self, type: RequestType, cancelled: CancelledType, message: str, superior_message: str,
                 request_date: str, response_date: str, employee_id):
        self.type = type
        self.cancelled = cancelled
        self.message = message
        self.superior_message = superior_message
        self.request_date = request_date
        self.response_date = response_date
        self.employee_id = employee_id
