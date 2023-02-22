from datetime import date

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.employees.exceptions import *
from app.employees.models import Employee


class EmployeeRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_employee(self, email, password, first_name, last_name, date_of_birth, phone_number,
                        street_name, city, postal_code, country, holiday_group_id, superior_id, days_off):
        try:
            employee = Employee(email=email, password=password, first_name=first_name, last_name=last_name,
                                date_of_birth=date_of_birth, phone_number=phone_number, street_name=street_name,
                                city=city, postal_code=postal_code, country=country, holiday_group_id=holiday_group_id,
                                superior_id=superior_id, days_off=days_off)
            self.db.add(employee)
            self.db.commit()
            self.db.refresh(employee)
            return employee
        except IntegrityError as e:
            raise e

    def get_employee_by_id(self, employee_id: str):
        employee = self.db.query(Employee).filter(Employee.id == employee_id).first()
        if employee is None:
            raise EmployeeNotFoundException(f"Employee with provided ID: *** {employee_id} *** not found.", 400)
        return employee

    def get_employee_by_email(self, email: str):
        employee = self.db.query(Employee).filter(Employee.email == email).first()
        return employee

    def get_all_employees(self):
        employee = self.db.query(Employee).all()
        return employee

    def delete_employee_by_id(self, employee_id: str):
        try:
            employee = self.db.query(Employee).filter(Employee.id == employee_id).first()
            if employee is None:
                raise EmployeeNotFoundException(f"Employee with provided ID: *** {employee_id} *** not found.", 400)
            self.db.delete(employee)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update_employee(self,
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
                        days_off: int = None):
        try:
            employee = self.db.query(Employee).filter(Employee.id == employee_id).first()
            if employee is None:
                raise EmployeeNotFoundException(f"Employee with provided ID *** {employee_id} *** not found.", 400)
            if email is not None:
                employee.email = email
            if password is not None:
                employee.password = password
            if first_name is not None:
                employee.first_name = first_name
            if last_name is not None:
                employee.last_name = last_name
            if date_of_birth is not None:
                employee.date_of_birth = date_of_birth
            if phone_number is not None:
                employee.phone_number = phone_number
            if street_name is not None:
                employee.street_name = street_name
            if city is not None:
                employee.city = city
            if postal_code is not None:
                employee.postal_code = postal_code
            if country is not None:
                employee.country = country
            if holiday_group_id is not None:
                employee.holiday_group_id = holiday_group_id
            if superior_id is not None:
                employee.superior_id = superior_id
            if days_off is not None:
                employee.days_off = days_off
            self.db.add(employee)
            self.db.commit()
            self.db.refresh(employee)
            return employee
        except Exception as e:
            raise e

    def update_employee_add_day(self, employee_id: str, amount: int = 1):
        try:
            employee = self.db.query(Employee).filter(Employee.id == employee_id).first()
            employee.days_off = employee.days_off + amount

            self.db.add(employee)
            self.db.commit()
            self.db.refresh(employee)
            return employee
        except Exception as e:
            raise e

    def update_employee_remove_day(self, employee_id: str):
        try:
            employee = self.db.query(Employee).filter(Employee.id == employee_id).first()
            employee.days_off = employee.days_off - 1

            self.db.add(employee)
            self.db.commit()
            self.db.refresh(employee)
            return employee
        except Exception as e:
            raise e
