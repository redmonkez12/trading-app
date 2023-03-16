import datetime

from fastapi import APIRouter

from app.responses.HealthcheckResponse import HealthcheckResponse

healthcheck_router = APIRouter(
    prefix="/healthcheck",
    tags=["Healthcheck"],
)


@healthcheck_router.get("/", response_model=HealthcheckResponse)
async def healthcheck():
    return {"status": "App is running", "last_update": datetime.datetime.now().isoformat()}
