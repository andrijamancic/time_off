from app.request_dates.exceptions.request_date_exceptions import RequestDateExceptionCode
from app.request_dates.models import RequestDate
from app.request_dates.repositories.request_dates_repository import RequestDateRepository
from app.db import SessionLocal
from datetime import date

from app.request_dates.schemas import RequestDateStatus


class RequestDateService:
    @staticmethod
    def create_request_date(r_date: date, status: RequestDateStatus, request_id: str, employee_id: str):
        try:
            with SessionLocal() as db:
                request_date_repository = RequestDateRepository(db)
                return request_date_repository.add_request_date(r_date, status, request_id, employee_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_all_requested_dates():
        try:
            with SessionLocal() as db:
                requested_dates_repository = RequestDateRepository(db)
                return requested_dates_repository.get_all_requested_dates()
        except Exception as e:
            raise e

    @staticmethod
    def get_requested_date_by_id(request_date_id: str):
        try:
            with SessionLocal() as db:
                requested_dates_repository = RequestDateRepository(db)
                return requested_dates_repository.get_requested_date_by_id(request_date_id)
        except Exception as e:
            raise e

    @staticmethod
    def delete_requested_date_by_id(request_date_id: str):
        try:
            with SessionLocal() as db:
                requested_date_repository = RequestDateRepository(db)
                requested_date_repository.delete_requested_date_by_id(request_date_id)
                return True
        except Exception as e:
            raise e

    @staticmethod
    def update_requested_date_by_id(request_date_id: str,
                                    r_date: date = None,
                                    status: RequestDateStatus = None,
                                    request_id: str = None,
                                    employee_id: str = None):
        try:
            with SessionLocal() as db:
                request = RequestDateRepository(db)
                return request.update_requested_date_by_id(request_date_id, r_date,
                                                           status, request_id, employee_id)
        except Exception as e:
            raise e
