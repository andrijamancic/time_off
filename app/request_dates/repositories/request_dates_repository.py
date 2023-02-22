from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from datetime import date

from app.request_dates.exceptions import RequestDateNotFoundException
from app.request_dates.models import RequestDate
from app.request_dates.schemas import RequestDateStatus


class RequestDateRepository:
    def __init__(self, db: Session):
        self.db = db

    def add_request_date(self, r_date: date, status: RequestDateStatus, request_id: str, employee_id: str):
        """
        It adds a request date to the database

        :param r_date: date
        :type r_date: date
        :param status: RequestDateStatus = RequestDateStatus.PENDING
        :type status: RequestDateStatus
        :param request_id: The id of the request that the request date is associated with
        :type request_id: str
        :param employee_id: str
        :type employee_id: str
        :return: The request date
        """
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
        """
        It adds a request date to the database

        :param r_date: date
        :type r_date: date
        :param request_id: The id of the request that the employee is making
        :type request_id: str
        :param employee_id: str
        :type employee_id: str
        :return: The request date object
        """
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
        """
        It returns all the RequestDate objects in the database
        :return: A list of all the RequestDate objects in the database.
        """
        requested_dates = self.db.query(RequestDate).all()
        return requested_dates

    def get_calendar(self):
        """
        It returns a dictionary of lists of dates, where the key is the employee's name and the value is a list of dates
        that employee has requested
        :return: A dictionary with the employee id as the key and a list of dates as the value.
        """
        requested_dates = self.db.query(RequestDate).all()

        res = {}
        for date in requested_dates:
            key = date.employee_id + ' - ' + date.employee.first_name + ' ' + date.employee.last_name
            res.setdefault(key, [])
            res[key].append(date.r_date)
            res[key].append(date.status)

        return res

    def get_requested_date_by_id(self, requested_date_id: str):
        """
        It gets a requested date by ID

        :param requested_date_id: The ID of the requested date
        :type requested_date_id: str
        :return: A RequestDate object
        """
        requested_date = self.db.query(RequestDate).filter(RequestDate.id == requested_date_id).first()
        if requested_date is None:
            raise RequestDateNotFoundException(f"Request date with ID: {requested_date_id} not found.", 400)
        return requested_date

    def get_absent_today(self):
        """
        It returns a list of employees who are absent today
        :return: A list of employees who are absent today.
        """
        today = date.today()
        requested_dates = self.db.query(RequestDate).filter((RequestDate.r_date == today),
                                                            (RequestDate.status == RequestDateStatus.approved)).all()

        employees = list(map(lambda x: x.employee, requested_dates))

        return employees

    def get_requested_dates_by_employee_id(self, employee_id: str):
        """
        It returns a list of RequestDate objects that have the same employee_id as the employee_id passed in

        :param employee_id: str
        :type employee_id: str
        :return: A list of RequestDate objects
        """
        requested_dates = self.db.query(RequestDate).filter(RequestDate.employee_id == employee_id).all()

        return requested_dates

    def get_requested_dates_by_request_id(self, request_id: str):
        """
        It returns a list of RequestDate objects that have a status of approved and are associated with a specific
        request_id

        :param request_id: str
        :type request_id: str
        :return: A list of RequestDate objects
        """
        requested_dates = self.db.query(RequestDate).filter(RequestDate.request_id == request_id,
                                                            RequestDate.status == RequestDateStatus.approved)\
            .order_by(RequestDate.r_date.asc()).all()

        return requested_dates

    def delete_requested_date_by_id(self, requested_date_id: str):
        """
        It deletes a requested date from the database

        :param requested_date_id: The ID of the requested date to be deleted
        :type requested_date_id: str
        :return: A boolean value.
        """
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
        """

        :param request_date_id:
        :param r_date:
        :param status:
        :param request_id:
        :param employee_id:
        :return:
        """
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
        """
        It updates the status of a request date by its ID

        :param request_date_id: The ID of the request date to be updated
        :type request_date_id: str
        :param status: RequestDateStatus
        :type status: RequestDateStatus
        :return: A RequestDate object
        """
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
