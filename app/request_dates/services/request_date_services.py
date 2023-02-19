from app.employees.repositories.employee_repository import EmployeeRepository
from app.request_dates.exceptions.request_date_exceptions import RequestDateExceptionCode, WrongSuperiorException, \
    NoDaysException, RequestDateAlreadyApprovedException
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
    def employee_create_request_date(r_date: date, request_id: str, employee_id: str):
        try:
            with SessionLocal() as db:
                request_date_repository = RequestDateRepository(db)
                employee_repository = EmployeeRepository(db)

                employee = employee_repository.get_employee_by_id(employee_id)

                if employee.days_off == 0:
                    raise NoDaysException(f"Employee with ID: {employee_id} used all their days.", 400)

                return request_date_repository.employee_add_request_date(r_date, request_id, employee_id)
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
    def get_calendar():
        try:
            with SessionLocal() as db:
                requested_dates_repository = RequestDateRepository(db)
                return requested_dates_repository.get_calendar()
        except Exception as e:
            raise e

    @staticmethod
    def get_absent_today():
        try:
            with SessionLocal() as db:
                requested_dates_repository = RequestDateRepository(db)
                return requested_dates_repository.get_absent_today()
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
    def get_requested_dates_by_employee_id(employee_id: str):
        try:
            with SessionLocal() as db:
                employee_repository = EmployeeRepository(db)
                requested_dates_repository = RequestDateRepository(db)

                employee_repository.get_employee_by_id(employee_id)

                return requested_dates_repository.get_requested_dates_by_employee_id(employee_id)
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

    @staticmethod
    def superior_update_requested_date_by_id(request_date_id: str, superior_id: str, status: RequestDateStatus):
        try:
            with SessionLocal() as db:
                requested_dates_repository = RequestDateRepository(db)
                employee_repository = EmployeeRepository(db)

                employee_repository.get_employee_by_id(superior_id)

                request_date = requested_dates_repository.get_requested_date_by_id(request_date_id)

                expected_superior = request_date.employee.superior_id

                if expected_superior is not None and expected_superior != superior_id:
                    raise WrongSuperiorException(f"Request date with ID: {request_date_id} is not under this superior.",
                                                 400)

                if request_date.status == RequestDateStatus.approved:
                    raise RequestDateAlreadyApprovedException(f"Requested date already approved", 400)
                elif status == RequestDateStatus.approved:
                    employee_repository.update_employee_remove_day(request_date.employee_id)

                return requested_dates_repository.superior_update_request_date_by_id(request_date_id, status)
        except Exception as e:
            raise e
