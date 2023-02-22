from datetime import date
from app.employees.repositories import EmployeeRepository
from app.request_dates.exceptions import WrongSuperiorException, \
    NoDaysException, RequestDateAlreadyApprovedException
from app.request_dates.repositories import RequestDateRepository
from app.db import SessionLocal

from app.request_dates.schemas import RequestDateStatus


class RequestDateService:
    @staticmethod
    def create_request_date(r_date: date, status: RequestDateStatus, request_id: str, employee_id: str):
        """
        It creates a request date object and adds it to the database

        :param r_date: date - the date of the request
        :type r_date: date
        :param status: RequestDateStatus = RequestDateStatus.PENDING
        :type status: RequestDateStatus
        :param request_id: The id of the request that the request date is associated with
        :type request_id: str
        :param employee_id: the id of the employee who is requesting the date
        :type employee_id: str
        :return: A RequestDate object
        """
        try:
            with SessionLocal() as db:
                request_date_repository = RequestDateRepository(db)
                return request_date_repository.add_request_date(r_date, status, request_id, employee_id)
        except Exception as e:
            raise e

    @staticmethod
    def employee_create_request_date(r_date: date, request_id: str, employee_id: str):
        """
        It takes a date, a request ID, and an employee ID, and then it creates a request date for the employee

        :param r_date: date - the date the employee wants to take off
        :type r_date: date
        :param request_id: str
        :type request_id: str
        :param employee_id: str
        :type employee_id: str
        :return: The return value is the request date object that was created.
        """
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
        """
        It gets all the requested dates from the database
        :return: A list of all the requested dates
        """
        try:
            with SessionLocal() as db:
                requested_dates_repository = RequestDateRepository(db)
                return requested_dates_repository.get_all_requested_dates()
        except Exception as e:
            raise e

    @staticmethod
    def get_calendar():
        """
        It gets the calendar
        :return: A list of dates that are in the database.
        """
        try:
            with SessionLocal() as db:
                requested_dates_repository = RequestDateRepository(db)
                return requested_dates_repository.get_calendar()
        except Exception as e:
            raise e

    @staticmethod
    def get_absent_today():
        """
        It gets all the dates that are absent today
        :return: A list of all the users that are absent today.
        """
        try:
            with SessionLocal() as db:
                requested_dates_repository = RequestDateRepository(db)
                return requested_dates_repository.get_absent_today()
        except Exception as e:
            raise e

    @staticmethod
    def get_requested_date_by_id(request_date_id: str):
        """
        It gets a requested date by id

        :param request_date_id: str
        :type request_date_id: str
        :return: A list of RequestedDate objects
        """
        try:
            with SessionLocal() as db:
                requested_dates_repository = RequestDateRepository(db)
                return requested_dates_repository.get_requested_date_by_id(request_date_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_requested_dates_by_employee_id(employee_id: str):
        """
        It gets the requested dates by employee id

        :param employee_id: str
        :type employee_id: str
        :return: A list of RequestedDates objects
        """
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
        """
        It deletes a requested date by id

        :param request_date_id: str
        :type request_date_id: str
        :return: A boolean value.
        """
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

        """
        :param request_date_id:
        :param r_date:
        :param status:
        :param request_id:
        :param employee_id:
        :return:
        """
        try:
            with SessionLocal() as db:
                request = RequestDateRepository(db)
                return request.update_requested_date_by_id(request_date_id, r_date,
                                                           status, request_id, employee_id)
        except Exception as e:
            raise e

    @staticmethod
    def superior_update_requested_date_by_id(request_date_id: str, superior_id: str, status: RequestDateStatus):
        """
        It updates the status of a requested date by its ID, and if the status is approved, it removes a day from the
        employee's days off

        :param request_date_id: str, superior_id: str, status: RequestDateStatus
        :type request_date_id: str
        :param superior_id: str - the id of the superior who is approving the request
        :type superior_id: str
        :param status: RequestDateStatus
        :type status: RequestDateStatus
        :return: The return value is the updated requested date.
        """
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
                    raise RequestDateAlreadyApprovedException("Requested date already approved", 400)

                if status == RequestDateStatus.approved:
                    employee_repository.update_employee_remove_day(request_date.employee_id)

                return requested_dates_repository.superior_update_request_date_by_id(request_date_id, status)
        except Exception as e:
            raise e
