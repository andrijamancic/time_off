from datetime import date
from fastapi import HTTPException, Response
from app.employees.exceptions import EmployeeNotFoundException
from app.request_dates.exceptions import RequestDateNotFoundException
from app.request_dates.schemas import RequestDateStatus
from app.request_dates.services.request_date_services import RequestDateService
from app.employees.services.email_services import EmailServices
from pydantic import EmailStr


class RequestDateController:
    @staticmethod
    def create_request_date(r_date: date, status: RequestDateStatus, request_id: str, employee_id: str):
        """
        It creates a request date.

        :param r_date: date
        :type r_date: date
        :param status: RequestDateStatus = RequestDateStatus.PENDING
        :type status: RequestDateStatus
        :param request_id: The id of the request that the requested date is associated with
        :type request_id: str
        :param employee_id: str
        :type employee_id: str
        :return: A RequestDate object
        """
        try:
            requested_date = RequestDateService.create_request_date(r_date, status, request_id, employee_id)
            return requested_date
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def employee_create_request_date(r_date: date, request_id: str, employee_id: str):
        """
        It creates a request date for an employee.

        :param r_date: date
        :type r_date: date
        :param request_id: The id of the request that the employee is requesting a date for
        :type request_id: str
        :param employee_id: str
        :type employee_id: str
        :return: The requested date is being returned.
        """
        try:
            requested_date = RequestDateService.employee_create_request_date(r_date, request_id, employee_id)
            return requested_date
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_requested_dates():
        """
        It gets all the requested dates from the database
        :return: A list of all the requested dates
        """
        try:
            requested_dates = RequestDateService.get_all_requested_dates()
            return requested_dates
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_requested_date_by_id(request_date_id: str):
        """
        It gets a requested date by id.

        :param request_date_id: The id of the requested date
        :type request_date_id: str
        :return: A RequestedDate object
        """
        try:
            requested_date = RequestDateService.get_requested_date_by_id(request_date_id)
            if requested_date:
                return requested_date
        except RequestDateNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_requested_dates_by_employee_id(employee_id: str):
        """
        It gets the requested dates by employee id

        :param employee_id: str
        :type employee_id: str
        :return: A list of requested dates
        """
        try:
            requested_dates = RequestDateService.get_requested_dates_by_employee_id(employee_id)
            if requested_dates:
                return requested_dates
        except EmployeeNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_calendar():
        """
        It gets the calendar
        :return: A list of dates that have been requested.
        """
        try:
            requested_dates = RequestDateService.get_calendar()
            if requested_dates:
                return requested_dates
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_absent_today():
        """
        It gets the absent today
        :return: A list of all the employees that are absent today.
        """
        try:
            requested_dates = RequestDateService.get_absent_today()
            if requested_dates:
                return requested_dates
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_requested_date_by_id(request_date_id: str):
        """
        It deletes a requested date by id.

        :param request_date_id: str - the id of the requested date to be deleted
        :type request_date_id: str
        :return: A list of all the request dates
        """
        try:
            RequestDateService.delete_requested_date_by_id(request_date_id)
            return Response(content=f"Request date with id - {request_date_id} deleted successfully")
        except RequestDateNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def update_requested_date_by_id(request_date_id: str,
                                    r_date: date = None,
                                    status: RequestDateStatus = None,
                                    request_id: str = None,
                                    employee_id: str = None):
        '''

        :param request_date_id:
        :param r_date:
        :param status:
        :param request_id:
        :param employee_id:
        :return:
        '''
        try:
            request = RequestDateService.update_requested_date_by_id(request_date_id,
                                                                     r_date,
                                                                     status,
                                                                     request_id,
                                                                     employee_id)
            return request
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def superior_update_requested_date_by_id(request_date_id: str, superior_id: str, status: RequestDateStatus):
        """
        It updates the status of the requested date.

        :param request_date_id: str, superior_id: str, status: RequestDateStatus
        :type request_date_id: str
        :param superior_id: str - id of the superior
        :type superior_id: str
        :param status: RequestDateStatus
        :type status: RequestDateStatus
        :return: RequestDate object
        """
        try:
            request = RequestDateService.superior_update_requested_date_by_id(request_date_id, superior_id, status)
            if status == RequestDateStatus.approved:
                day = request.r_date.strftime("%Y-%m-%d")
                EmailServices.send_email(EmailStr(request.employee.email),
                                         "Odobren odmor", f"Odobren vam je odmor za dan {day}")
            return request
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
