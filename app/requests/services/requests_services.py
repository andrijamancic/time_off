from datetime import date

from sqlalchemy import Date

from app.db.database import SessionLocal
from app.employees.repositories.employee_repository import EmployeeRepository
from app.request_dates.repositories import RequestDateRepository
from app.requests.exceptions import EmptyRequestException, LateCancelException
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
    def create_employee_request(type, message, request_date, response_date, employee_id):
        try:
            with SessionLocal() as db:
                request_repository = RequestRepository(db)
                return request_repository.create_employee_request(type, message, request_date, response_date,
                                                                  employee_id)
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

    @staticmethod
    def update_request_to_cancelled(request_id: str):
        try:
            with SessionLocal() as db:
                request_repository = RequestRepository(db)
                request_date_repository = RequestDateRepository(db)
                employee_repository = EmployeeRepository(db)

                request_made = request_repository.get_request_by_id(request_id)

                request_dates = request_date_repository.get_requested_dates_by_request_id(request_id)

                if len(request_dates) == 0:
                    raise EmptyRequestException(f"Request with ID: {request_id} has no requested days.", 400)

                first_day = request_dates[0]
                num_days = len(request_dates)

                if date.today() > first_day.r_date:
                    raise LateCancelException(f"Request with ID: {request_id} has already"
                                              f" started and you cannot cancel.", 400)

                employee_repository.update_employee_add_day(request_made.employee_id, num_days)

                return request_repository.update_request_to_cancelled(request_id)
        except Exception as e:
            raise e
