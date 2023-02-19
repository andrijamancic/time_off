from datetime import date

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.requests.exceptions import RequestNotFoundException
from app.requests.models import Request
from app.requests.schemas import RequestType


class RequestRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_request(self, type, cancelled, message, superior_message, request_date, response_date, employee_id):
        try:
            request = Request(type, cancelled, message, superior_message, request_date, response_date, employee_id)
            self.db.add(request)
            self.db.commit()
            self.db.refresh(request)
            return request
        except IntegrityError as e:
            raise e

    def create_employee_request(self, type, message, request_date, response_date, employee_id):
        try:
            request = Request(type, None, message, None, request_date, response_date, employee_id)
            self.db.add(request)
            self.db.commit()
            self.db.refresh(request)
            return request
        except IntegrityError as e:
            raise e

    def get_all_requests(self):
        request = self.db.query(Request).all()
        return request

    def get_request_by_id(self, request_id: str):
        request = self.db.query(Request).filter(Request.id == request_id).first()
        if request is None:
            raise RequestNotFoundException(f"Request with ID: {request_id} not found.", 400)
        return request

    def delete_request_by_id(self, request_id: str):
        try:
            request = self.db.query(Request).filter(Request.id == request_id).first()
            if request is None:
                raise RequestNotFoundException(
                    f"Request with ID: {request_id} not found.", 400,)
            self.db.delete(request)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update_request_by_id(self, request_id: str,
                             type: RequestType = None,
                             cancelled: bool = None,
                             message: str = None,
                             superior_message: str = None,
                             request_date: date = None,
                             response_date: date = None,
                             employee_id: str = None):
        try:
            request = self.db.query(Request).filter(Request.id == request_id).first()
            if request is None:
                raise RequestNotFoundException(f"Request with ID: {request_id}  not found.", 400)
            if type is not None:
                request.type = type
            if cancelled is not None:
                request.cancelled = cancelled
            if message is not None:
                request.message = message
            if superior_message is not None:
                request.superior_message = superior_message
            if request_date is not None:
                request.request_date = request_date
            if response_date is not None:
                request.response_date = response_date
            if employee_id is not None:
                request.employee_id = employee_id
            self.db.add(request)
            self.db.commit()
            self.db.refresh(request)
            return request
        except Exception as e:
            raise e

    def update_request_to_cancelled(self, request_id: str):
        try:
            request = self.db.query(Request).filter(Request.id == request_id).first()

            if request is None:
                raise RequestNotFoundException(f"Request with ID: {request_id}  not found.", 400)

            request.cancelled = True

            self.db.add(request)
            self.db.commit()
            self.db.refresh(request)
            return request
        except Exception as e:
            raise e
