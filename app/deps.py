from app.services.MarketService import MarketService
from app.services.UserService import UserService
from database import async_session


async def get_user_service():
    async with async_session() as session:
        async with session.begin():
            yield UserService(session)


async def get_instrument_service():
    async with async_session() as session:
        async with session.begin():
            yield MarketService(session)
