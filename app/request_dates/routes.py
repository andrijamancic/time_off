from typing import Optional

from fastapi import APIRouter, Depends
from datetime import date

from app.employees.controller.employee_auth_controller import JWTBearer
from app.employees.schemas.employee_schemas import EmployeeSchema
from app.request_dates.controller.request_date_controller import RequestDateController

from app.request_dates.schemas import RequestDateSchema, RequestDateSchemaIn, RequestDateStatus, \
    EmployeeRequestDateSchema

request_date_router = APIRouter(tags=["request_dates"], prefix="/api/request_dates")


@request_date_router.post("/create-request-date/employee", response_model=RequestDateSchema)
def employee_create_request_date(request_date: EmployeeRequestDateSchema):
    return RequestDateController.employee_create_request_date(request_date.r_date, request_date.request_id,
                                                              request_date.employee_id)


@request_date_router.post("/create-request-date", response_model=RequestDateSchema,
                          dependencies=[Depends(JWTBearer("superior_employee"))])
def create_request_date(request_date: RequestDateSchemaIn):
    return RequestDateController.create_request_date(request_date.r_date, request_date.status, request_date.request_id,
                                                     request_date.employee_id)


@request_date_router.get("/get-all-requested_dates", response_model=list[RequestDateSchema],
                         dependencies=[Depends(JWTBearer("superior_employee"))])
def get_all_requested_dates():
    return RequestDateController.get_all_requested_dates()


@request_date_router.get("/id", response_model=RequestDateSchema)
def get_requested_date_by_id(request_date_id: str):
    return RequestDateController.get_requested_date_by_id(request_date_id)


@request_date_router.get("/employee-id", response_model=list[RequestDateSchema])
def get_requested_dates_by_employee_id(employee_id: str):
    return RequestDateController.get_requested_dates_by_employee_id(employee_id)


@request_date_router.get("/all-employees-calendar", response_model=dict,
                         dependencies=[Depends(JWTBearer("superior_employee"))])
def all_employees_calendar():
    return RequestDateController.get_calendar()


@request_date_router.get("/all-employees-absent-today", response_model=Optional[list[EmployeeSchema]],
                         dependencies=[Depends(JWTBearer("superior_employee"))])
def all_employees_absent_today():
    return RequestDateController.get_absent_today()


@request_date_router.delete("/", dependencies=[Depends(JWTBearer("superior_employee"))])
def delete_requested_date_by_id(request_date_id: str):
    return RequestDateController.delete_requested_date_by_id(request_date_id)


@request_date_router.put("/update", response_model=RequestDateSchema,
                         dependencies=[Depends(JWTBearer("superior_employee"))])
def update_requested_date_by_id(request_date_id: str, r_date: date = None, status: RequestDateStatus = None,
                                request_id: str = None, employee_id: str = None):
    return RequestDateController.update_requested_date_by_id(request_date_id, r_date, status, request_id,
                                                             employee_id)


@request_date_router.put("/update/superior", response_model=RequestDateSchema,
                         dependencies=[Depends(JWTBearer("superior_employee"))])
def superior_update_requested_date_by_id(request_date_id: str, superior_id: str, status: RequestDateStatus):
    return RequestDateController.superior_update_requested_date_by_id(request_date_id, superior_id, status)
