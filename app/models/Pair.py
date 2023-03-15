from sqlmodel import SQLModel, Field

from app.models.Instrument import Instrument
import sqlalchemy as sa


class Pair(SQLModel, table=True):
    __tablename__ = "pairs"

    pair_id: int = Field(default=True, primary_key=True)
    name: str = Field(sa_column=sa.Column(sa.TEXT, nullable=False))
    instrument_id: int = Field(
        sa_column=sa.Column(sa.Integer, sa.ForeignKey(Instrument.instrument_id, ondelete="CASCADE")), nullable=False)
