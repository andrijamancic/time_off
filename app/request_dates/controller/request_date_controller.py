from fastapi import HTTPException, Response

from app.request_dates.exceptions.request_date_exceptions import RequestDateExceptionCode, RequestDateNotFoundException
from app.request_dates.services import request_date_services


class RequestDateController:
    @staticmethod
    def create_new_course(code: str, name: str, description: str):
        try:
            course = CourseService.create_new_course(code, name, description)
            return course
        except CourseExceptionCode as e:
            print(e)
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
