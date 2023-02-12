from app.request_dates.exceptions.request_date_exceptions import RequestDateExceptionCode
from app.request_dates.models import RequestDate
from app.request_dates.repositories.request_dates_repository import RequestDateRepository
from app.db import SessionLocal
from datetime import date


class CourseService:
    @staticmethod
    def add_date_to_request_date_off(date): # -> CourseExceptionCode or Course:
        try:
            with SessionLocal() as db:
                request_date = RequestDateRepository(db)
                # request_date = request_date.read_course_by_code(code)
                if request_date is None:
                    return request_date.add_request_date(date)
                raise RequestDateExceptionCode(message="date already booked.", code=400)
        except Exception as e:
            raise e