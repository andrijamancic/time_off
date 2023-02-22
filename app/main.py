import uvicorn
from fastapi import FastAPI
from starlette.responses import RedirectResponse
from app.db.database import engine, Base
from app.employees.routes import employee_router, login_router
from app.holiday_group_dates.routes import holiday_group_dates_router
from app.holiday_groups.routes import holiday_group_router
from app.request_dates.routes import request_date_router
from app.requests.routes import request_router

Base.metadata.create_all(bind=engine)


def init_app():
    app = FastAPI()
    app.include_router(login_router)
    app.include_router(holiday_group_router)
    app.include_router(holiday_group_dates_router)
    app.include_router(employee_router)
    app.include_router(request_router)
    app.include_router(request_date_router)

    return app


app = init_app()


@app.get("/", include_in_schema=False)
def start():
    return RedirectResponse('/docs')


if __name__ == "__main__":
    uvicorn.run(app)
