from fastapi import APIRouter, Depends, Query, status
from pydantic import Required

from app.auth.user import get_current_user
from app.deps import get_instrument_service
from app.models.User import User
from app.services.MarketService import MarketService

market_router = APIRouter(
    prefix="/markets",
    tags=["Markets"],
)


@market_router.get("/", status_code=status.HTTP_200_OK)
async def get_markets(*, instrument_service: MarketService = Depends(get_instrument_service),
                      per_page: int = Query(default=Required),
                      page: int = Query(default=Required),
                      ):
    return await instrument_service.get_markets(page, per_page)
