from datetime import date

from fastapi import APIRouter, Depends

from app.employees.controller.employee_auth_controller import JWTBearer
from app.employees.controller.employee_controller import EmployeeController

from app.employees.schemas.employee_schemas import EmployeeSchema, EmployeeSchemaIn, EmployeeLoginSchema

employee_router = APIRouter(tags=["employees"], prefix="/api/employees")
login_router = APIRouter(tags=["LogIn"])


@login_router.post("/login")
def login_employee(employee: EmployeeLoginSchema):
    return EmployeeController.login_employee(employee.email, employee.password)


@employee_router.post("/add-new-employee", response_model=EmployeeSchema)
def create_employee(employee: EmployeeSchemaIn):
    return EmployeeController.create_employee(employee.email,
                                              employee.password,
                                              employee.first_name,
                                              employee.last_name,
                                              employee.date_of_birth,
                                              employee.phone_number,
                                              employee.street_name,
                                              employee.city,
                                              employee.postal_code,
                                              employee.country,
                                              employee.holiday_group_id,
                                              employee.superior_id,
                                              employee.days_off)


@employee_router.get("/id", response_model=EmployeeSchema, dependencies=[Depends(JWTBearer("superior_employee"))])
def get_employee_by_id(employee_id: str):
    return EmployeeController.get_employee_by_id(employee_id)


@employee_router.get("/get-all-employees", response_model=list[EmployeeSchema])
def get_all_employees():
    return EmployeeController.get_all_employees()


@employee_router.delete("/", dependencies=[Depends(JWTBearer("superior_employee"))])
def delete_employee_by_id(employee_id: str):
    return EmployeeController.delete_employee_by_id(employee_id)


@employee_router.put("/update-employee-by-id", response_model=EmployeeSchema,
                     dependencies=[Depends(JWTBearer("superior_employee"))])
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
    return EmployeeController.update_employee(employee_id, email, password, first_name, last_name, date_of_birth,
                                              phone_number, street_name, city, postal_code, country, holiday_group_id,
                                              superior_id, days_off)
