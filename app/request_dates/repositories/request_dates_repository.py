from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from datetime import date

from app.request_dates.exceptions import RequestDateNotFoundException
# from app.request_dates.exceptions.request_date_exceptions import RequestDateNotFoundException
from app.request_dates.models import RequestDate
from app.request_dates.schemas import RequestDateStatus


class RequestDateRepository:
    def __init__(self, db: Session):
        self.db = db

    def add_request_date(self, r_date: date, status: RequestDateStatus, request_id: str, employee_id: str):
        try:
            request_date = RequestDate(r_date, status, request_id, employee_id)
            self.db.add(request_date)
            self.db.commit()
            self.db.refresh(request_date)
            return request_date
        except IntegrityError as e:
            raise e
        except Exception as e:
            raise e

    def employee_add_request_date(self, r_date: date, request_id: str, employee_id: str):
        try:
            request_date = RequestDate(r_date, RequestDateStatus.pending, request_id, employee_id)
            self.db.add(request_date)
            self.db.commit()
            self.db.refresh(request_date)
            return request_date
        except IntegrityError as e:
            raise e
        except Exception as e:
            raise e

    def get_all_requested_dates(self):
        requested_dates = self.db.query(RequestDate).all()
        return requested_dates

    def get_calendar(self):
        requested_dates = self.db.query(RequestDate).all()

        res = {}
        for date in requested_dates:
            key = date.employee_id + ' - ' + date.employee.first_name + ' ' + date.employee.last_name
            res.setdefault(key, [])
            res[key].append(date.r_date)

        return res

    def get_requested_date_by_id(self, requested_date_id: str):
        requested_date = self.db.query(RequestDate).filter(RequestDate.id == requested_date_id).first()
        if requested_date is None:
            raise RequestDateNotFoundException(f"Request date with ID: {requested_date_id} not found.", 400)
        return requested_date

    def get_absent_today(self):
        today = date.today()
        requested_dates = self.db.query(RequestDate).filter((RequestDate.r_date == today),
                                                            (RequestDate.status == RequestDateStatus.approved)).all()

        employees = list(map(lambda x: x.employee, requested_dates))

        return employees

    def get_requested_dates_by_employee_id(self, employee_id: str):
        requested_dates = self.db.query(RequestDate).filter(RequestDate.employee_id == employee_id).all()

        return requested_dates

    def get_requested_dates_by_request_id(self, request_id: str):
        requested_dates = self.db.query(RequestDate).filter(RequestDate.request_id == request_id,
                                                            RequestDate.status == RequestDateStatus.approved)\
            .order_by(RequestDate.r_date.asc()).all()

        return requested_dates

    def delete_requested_date_by_id(self, requested_date_id: str):
        try:
            request = self.db.query(RequestDate).filter(RequestDate.id == requested_date_id).first()
            if request is None:
                raise RequestDateNotFoundException(
                    f"Request with ID: {requested_date_id} not found.", 400,)
            self.db.delete(request)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update_requested_date_by_id(self, request_date_id: str, r_date: date = None,
                                    status: RequestDateStatus = None,
                                    request_id: str = None,
                                    employee_id: str = None):
        try:
            requested_date = self.db.query(RequestDate).filter(RequestDate.id == request_date_id).first()
            if requested_date is None:
                raise RequestDateNotFoundException(f"Request date with ID: {request_date_id}  not found.", 400)
            if r_date is not None:
                requested_date.r_date = r_date
            if status is not None:
                requested_date.status = status
            if request_id is not None:
                requested_date.request_id = request_id
            if employee_id is not None:
                requested_date.employee_id = employee_id
            self.db.add(requested_date)
            self.db.commit()
            self.db.refresh(requested_date)
            return requested_date
        except Exception as e:
            raise e

    def superior_update_request_date_by_id(self, request_date_id: str, status: RequestDateStatus):
        try:
            requested_date = self.db.query(RequestDate).filter(RequestDate.id == request_date_id).first()
            if requested_date is None:
                raise RequestDateNotFoundException(f"Request date with ID: {request_date_id}  not found.", 400)

            requested_date.status = status

            self.db.add(requested_date)
            self.db.commit()
            self.db.refresh(requested_date)
            return requested_date
        except Exception as e:
            raise e
