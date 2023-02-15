from datetime import date

from sqlalchemy import Date

from app.db.database import SessionLocal
from app.requests.repositories.request_repository import RequestRepository
from app.requests.schemas import RequestType


class RequestServices:
    @staticmethod
    def create_request(type, cancelled, message, superior_message, request_date, response_date, employee_id):
        try:
            with SessionLocal() as db:
                request_repository = RequestRepository(db)
                return request_repository.create_request(type, cancelled, message, superior_message, request_date,
                                                         response_date, employee_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_all_requests():
        try:
            with SessionLocal() as db:
                request_repository = RequestRepository(db)
                return request_repository.get_all_requests()
        except Exception as e:
            raise e

    @staticmethod
    def get_request_by_id(request_id: str):
        try:
            with SessionLocal() as db:
                request_repository = RequestRepository(db)
                return request_repository.get_request_by_id(request_id)
        except Exception as e:
            raise e

    @staticmethod
    def delete_request_by_id(request_id: str):
        try:
            with SessionLocal() as db:
                request_repository = RequestRepository(db)
                request_repository.delete_request_by_id(request_id)
                return True
        except Exception as e:
            raise e

    @staticmethod
    def update_request_by_id(request_id: str,
                             type: RequestType = None,
                             cancelled: bool = None,
                             message: str = None,
                             superior_message: str = None,
                             request_date: date = None,
                             response_date: date = None,
                             employee_id: str = None):
        try:
            with SessionLocal() as db:
                request = RequestRepository(db)
                return request.update_request_by_id(request_id, type, cancelled, message, superior_message,
                                                    request_date, response_date, employee_id)
        except Exception as e:
            raise e
