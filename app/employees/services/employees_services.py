from datetime import date

from app.db.database import SessionLocal
from app.employees.repositories.employee_repository import EmployeeRepository


class EmployeeServices:
    @staticmethod
    def create_employee(email, password, first_name, last_name, date_of_birth, phone_number,
                        street_name, city, postal_code, country, holiday_group_id, superior_id, days_off):
        try:
            with SessionLocal() as db:
                employee_repository = EmployeeRepository(db)
                return employee_repository.create_employee(email, password, first_name, last_name, date_of_birth,
                                                           phone_number, street_name, city, postal_code, country,
                                                           holiday_group_id, superior_id, days_off)
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
                return employee_repository.update_employee(employee_id, email, password, first_name, last_name,
                                                        date_of_birth, phone_number, street_name, city, postal_code,
                                                        country, holiday_group_id, superior_id, days_off)
        except Exception as e:
            raise e
