from fastapi import HTTPException, Response, status
from datetime import date
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