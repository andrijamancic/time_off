from datetime import date

from fastapi import HTTPException, Response, status

from app.employees.exceptions import *
from app.employees.services import EmployeeServices


class EmployeeController:
    @staticmethod
    def create_employee(email, password, first_name, last_name, date_of_birth, phone_number,
                        street_name, city, postal_code, country, holiday_group_id, superior_id, days_off):
        try:
            employee = EmployeeServices.create_employee(email, password, first_name, last_name, date_of_birth,
                                                        phone_number, street_name, city, postal_code, country,
                                                        holiday_group_id, superior_id, days_off)
            return employee
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    # @staticmethod
    # def get_employee_by_id(employee_id: str):
    #     employee = EmployeeServices.get_employee_by_id(employee_id)
    #     if employee:
    #         return employee
    #     raise HTTPException(
    #         status_code=status.HTTP_400_BAD_REQUEST,
    #         detail=f"Employee with provided id *** {employee_id} *** does not exist",
    #     )
    @staticmethod
    def get_employee_by_id(employee_id: str):
        try:
            employee = EmployeeServices.get_employee_by_id(employee_id)
            if employee:
                return employee
        except EmployeeNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_employees():
        employee = EmployeeServices.get_all_employees()
        return employee

    @staticmethod
    def delete_employee_by_id(employee_id: str):
        try:
            EmployeeServices.delete_employee_by_id(employee_id)
            return Response(content=f"Employee with id *** {employee_id} *** deleted successfully")
        except EmployeeNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

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
            employee = EmployeeServices.update_employee(employee_id, email, password, first_name, last_name,
                                                        date_of_birth, phone_number, street_name, city, postal_code,
                                                        country, holiday_group_id, superior_id, days_off)
            return employee
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
