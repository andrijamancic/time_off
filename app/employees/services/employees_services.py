import hashlib
from datetime import date

from app.db.database import SessionLocal
from app.employees.exceptions import EmployeeInvalidPasswordException
from app.employees.repositories.employee_repository import EmployeeRepository


class EmployeeServices:
    @staticmethod
    def create_employee(email, password, first_name, last_name, date_of_birth, phone_number,
                        street_name, city, postal_code, country, holiday_group_id, superior_id, days_off):
        with SessionLocal() as db:
            try:
                employee_repository = EmployeeRepository(db)
                hashed_password = hashlib.sha256(bytes(password, "utf-8")).hexdigest()
                return employee_repository.create_employee(email=email, password=hashed_password,
                                                           first_name=first_name, last_name=last_name,
                                                           date_of_birth=date_of_birth, phone_number=phone_number,
                                                           street_name=street_name, city=city, postal_code=postal_code,
                                                           country=country, holiday_group_id=holiday_group_id,
                                                           superior_id=superior_id, days_off=days_off)
            except Exception as e:
                raise e

    @staticmethod
    def get_employee_by_id(employee_id: str):
        try:
            with SessionLocal() as db:
                employee_repository = EmployeeRepository(db)
                return employee_repository.get_employee_by_id(employee_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_all_employees():
        try:
            with SessionLocal() as db:
                employee_repository = EmployeeRepository(db)
                return employee_repository.get_all_employees()
        except Exception as e:
            raise e

    @staticmethod
    def delete_employee_by_id(employee_id: str):
        try:
            with SessionLocal() as db:
                employee_repository = EmployeeRepository(db)
                employee_repository.delete_employee_by_id(employee_id)
                return True
        except Exception as e:
            raise e

    @staticmethod
    def update_employee(
            employee_id: str,
            email: str = None,
            password: str = None,
            first_name: str = None,
            last_name: str = None,
            date_of_birth: date = None,
            phone_number: str = None,
            street_name: str = None,
            city: str = None,
            postal_code: str = None,
            country: str = None,
            holiday_group_id: str = None,
            superior_id: str = None,
            days_off: int = None
    ):
        try:
            with SessionLocal() as db:
                employee_repository = EmployeeRepository(db)
                if password is not None:
                    hashed_password = hashlib.sha256(bytes(password, "utf-8")).hexdigest()
                    return employee_repository.update_employee(employee_id, email, hashed_password, first_name,
                                                               last_name, date_of_birth, phone_number, street_name,
                                                               city, postal_code, country, holiday_group_id,
                                                               superior_id, days_off)
                else:
                    return employee_repository.update_employee(employee_id, email, password, first_name,
                                                               last_name, date_of_birth, phone_number, street_name,
                                                               city, postal_code, country, holiday_group_id,
                                                               superior_id, days_off)
        except Exception as e:
            raise e

    @staticmethod
    def login_employee(email: str, password: str):
        with SessionLocal() as db:
            try:
                user_repository = EmployeeRepository(db)
                user = user_repository.get_employee_by_email(email)
                if hashlib.sha256(bytes(password, "utf-8")).hexdigest() != user.password:
                    raise EmployeeInvalidPasswordException(message="Invalid password for employee", code=401)
                return user
            except Exception as e:
                raise e
