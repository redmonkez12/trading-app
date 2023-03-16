from sqlmodel import Session, select, func

from app.models.Market import Market


class MarketService:
    def __init__(self, session: Session):
        self.session = session

    async def get_markets(self, page: int, per_page: int) -> list[Market]:
        query = (
            select(Market)
            .limit(per_page)
            .offset(page * per_page)
        )

        result = await self.session.execute(query)

        total_query = select(func.count()).select_from(Market)
        count = await self.session.execute(total_query)

        return {"count": count.scalar(), "markets": result.scalars().all()}
