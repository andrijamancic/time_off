from fastapi import HTTPException, Response, status
from datetime import date

from app.employees.exceptions import EmployeeNotFoundException
from app.request_dates.exceptions import RequestDateNotFoundException
from app.request_dates.schemas import RequestDateStatus
from app.request_dates.services.request_date_services import RequestDateService


class RequestDateController:
    @staticmethod
    def create_request_date(r_date: date, status: RequestDateStatus, request_id: str, employee_id: str):
        try:
            requested_date = RequestDateService.create_request_date(r_date, status, request_id, employee_id)
            return requested_date
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def employee_create_request_date(r_date: date, request_id: str, employee_id: str):
        try:
            requested_date = RequestDateService.employee_create_request_date(r_date, request_id, employee_id)
            return requested_date
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_requested_dates():
        try:
            requested_dates = RequestDateService.get_all_requested_dates()
            return requested_dates
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_requested_date_by_id(request_date_id: str):
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
        try:
            requested_dates = RequestDateService.get_calendar()
            if requested_dates:
                return requested_dates
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_absent_today():
        try:
            requested_dates = RequestDateService.get_absent_today()
            if requested_dates:
                return requested_dates
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_requested_date_by_id(request_date_id: str):
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
        try:
            request = RequestDateService.superior_update_requested_date_by_id(request_date_id, superior_id, status)
            return request
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))