from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

# from app.request_dates.exceptions.request_date_exceptions import RequestDateNotFoundException
from app.request_dates.models import RequestDate


class RequestDateRepository:
    def __init__(self, db: Session):
        self.db = db

    def add_request_date(self, date: str):
        try:
            request_date = RequestDate(date)
            self.db.add(request_date)
            self.db.commit()
            self.db.refresh(request_date)
            return request_date
        except IntegrityError as e:
            raise e
        except Exception as e:
            raise e
