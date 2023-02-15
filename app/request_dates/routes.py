from fastapi import APIRouter, Depends
from datetime import date
from app.request_dates.controller.request_date_controller import RequestDateController

from app.request_dates.schemas import RequestDateSchema, RequestDateSchemaIn, RequestDateStatus

request_date_router = APIRouter(tags=["request_dates"], prefix="/api/request_dates")


@request_date_router.post("/create-request-date", response_model=RequestDateSchema)
def create_request_date(request_date: RequestDateSchemaIn):
    return RequestDateController.create_request_date(request_date.r_date, request_date.status, request_date.request_id,
                                                     request_date.employee_id)


@request_date_router.get("/get-all-requested_dates", response_model=list[RequestDateSchema])
def get_all_requested_dates():
    return RequestDateController.get_all_requested_dates()


@request_date_router.get("/id", response_model=RequestDateSchema)
def get_requested_date_by_id(request_date_id: str):
    return RequestDateController.get_requested_date_by_id(request_date_id)


@request_date_router.delete("/") # , dependencies=[Depends(JWTBearer("super_user"))])
def delete_requested_date_by_id(request_date_id: str):
    return RequestDateController.delete_requested_date_by_id(request_date_id)


@request_date_router.put("/update", response_model=RequestDateSchema) # , dependencies=[Depends(JWTBearer("super_user"))])
def update_requested_date_by_id(request_date_id: str, r_date: date = None, status: RequestDateStatus = None,
                                request_id: str = None, employee_id: str = None):
    return RequestDateController.update_requested_date_by_id(request_date_id, r_date, status, request_id,
                                                             employee_id)
