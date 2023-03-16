from sqlmodel import SQLModel, Field

import sqlalchemy as sa


class Market(SQLModel, table=True):
    __tablename__ = "markets"

    market_id: int = Field(default=True, primary_key=True)
    name: str = Field(sa_column=sa.Column(sa.TEXT, nullable=False))
