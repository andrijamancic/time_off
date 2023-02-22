from datetime import date
from fastapi import HTTPException, Response
from app.requests.exceptions import RequestNotFoundException
from app.requests.schemas import RequestType
from app.requests.services.requests_services import RequestServices


class RequestController:
    @staticmethod
    def create_request(type, cancelled, message, superior_message, request_date, response_date, employee_id):
        try:
            request = RequestServices.create_request(type, cancelled, message, superior_message, request_date,
                                                     response_date, employee_id)
            return request
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def create_employee_request(type, message, request_date, response_date, employee_id):
        try:
            request = RequestServices.create_employee_request(type, message, request_date, response_date, employee_id)
            return request
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def cancel_employee_request(request_id: str):
        try:
            request = RequestServices.update_request_to_cancelled(request_id)
            return request
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_requests():
        try:
            request = RequestServices.get_all_requests()
            return request
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_request_by_id(request_id: str):
        try:
            request = RequestServices.get_request_by_id(request_id)
            if request:
                return request
        except RequestNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_request_by_id(request_id: str):
        try:
            RequestServices.delete_request_by_id(request_id)
            return Response(content=f"Request with id - {request_id} deleted successfully")
        except RequestNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

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
            request = RequestServices.update_request_by_id(request_id, type, cancelled, message, superior_message,
                                                           request_date, response_date, employee_id)
            return request
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))