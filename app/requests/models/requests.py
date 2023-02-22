from typing import Optional
from uuid import uuid4
from datetime import date
from sqlalchemy import Column, String, Date, ForeignKey, Enum, Boolean
from app.db import Base
from app.requests.schemas import RequestType


class Request(Base):
    __tablename__ = "requests"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    type = Column(Enum(RequestType))
    cancelled = Column(Boolean, default=False)
    message = Column(String(250))
    superior_message = Column(String(250), default="")
    request_date = Column(Date)
    response_date = Column(Date)

    employee_id = Column(String(50), ForeignKey("employees.id"), nullable=False)

    def __init__(self, type: RequestType, cancelled: Optional[Boolean], message: str, superior_message: Optional[str],
                 request_date: date, response_date: date, employee_id: str):
        self.type = type
        self.cancelled = cancelled
        self.message = message
        self.superior_message = superior_message
        self.request_date = request_date
        self.response_date = response_date
        self.employee_id = employee_id
