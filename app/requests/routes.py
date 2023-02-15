from datetime import date

from fastapi import APIRouter, Depends

from app.requests.controller.request_controller import RequestController

from app.requests.schemas import RequestSchema, RequestSchemaIn, RequestType

request_router = APIRouter(tags=["requests"], prefix="/api/requests")


@request_router.post("/create-request", response_model=RequestSchema)
def create_request(request: RequestSchemaIn):
    return RequestController.create_request(request.type, request.cancelled, request.message, request.superior_message,
                                            request.request_date, request.response_date, request.employee_id)


@request_router.get("/get-all-requests", response_model=list[RequestSchema])
def get_all_requests():
    return RequestController.get_all_requests()


@request_router.get("/id", response_model=RequestSchema)
def get_request_by_id(request_id: str):
    return RequestController.get_request_by_id(request_id)


@request_router.delete("/") # , dependencies=[Depends(JWTBearer("super_user"))])
def delete_request_by_id(request_id: str):
    return RequestController.delete_request_by_id(request_id)


@request_router.put("/update", response_model=RequestSchema) # , dependencies=[Depends(JWTBearer("super_user"))])
def update_request_by_id(request_id,
                         type: RequestType = None,
                         cancelled: bool = None,
                         message: str = None,
                         superior_message: str = None,
                         request_date: date = None,
                         response_date: date = None,
                         employee_id: str = None):
    return RequestController.update_request_by_id(request_id, type, cancelled, message, superior_message, request_date,
                                                  response_date, employee_id)
