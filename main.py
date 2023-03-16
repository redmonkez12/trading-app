from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from app.controllers.others.Healthcheck import healthcheck_router
from app.controllers.markets.MarketController import market_router
from app.controllers.users.UsersController import user_router
from database import init_db

app = FastAPI(
    title="Forex analysis app",
    description="You can analyse your performance and portfolio",
    version="0.0.1",
)


@app.on_event("startup")
async def on_startup():
    await init_db()


@app.get("/")
async def main():
    return "App is running"


app.include_router(user_router, prefix="/api/v1")
app.include_router(healthcheck_router, prefix="/api/v1")
app.include_router(market_router, prefix="/api/v1")


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(_: Request, exc: RequestValidationError):
    errors = exc.errors()
    error = ""
    code = ""

    if len(errors) > 1:
        if errors[0]["msg"] == "field required":
            field = errors[0]['loc'][1]
            error = f"The field {field} is required"
            code = f"{field.upper()}_REQUIRED"

    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({
            "message": error,
            "code": code,
            "status": status.HTTP_422_UNPROCESSABLE_ENTITY,
        }),
    )
