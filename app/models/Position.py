import datetime

from sqlmodel import SQLModel, Field
import sqlalchemy as sa


class Position(SQLModel, table=True):
    __tablename__ = "positions"

    position_id: int = Field(default=True, primary_key=True)
    close_time: datetime.datetime = Field(sa_column=sa.Column(sa.DateTime(timezone=True), nullable=False))
    open_time: datetime.datetime = Field(sa_column=sa.Column(sa.DateTime(timezone=True), nullable=False))
    position_size: int = Field(nullable=False)
    open_price: float = Field(nullable=False)
    close_price: float = Field(nullable=False)
