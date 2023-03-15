from sqlmodel import SQLModel, Field

import sqlalchemy as sa


class Instrument(SQLModel, table=True):
    __tablename__ = "instruments"

    instrument_id: int = Field(default=True, primary_key=True)
    name: str = Field(sa_column=sa.Column(sa.TEXT, nullable=False))
