import datetime

from sqlmodel import SQLModel, Field

import sqlalchemy as sa


class User(SQLModel, table=True):
    __tablename__ = "users"

    user_id: int = Field(default=True, primary_key=True)
    first_name: str = Field(sa_column=sa.Column(sa.TEXT, nullable=False))
    last_name: str = Field(sa_column=sa.Column(sa.TEXT, nullable=False))
    email: str = Field(sa_column=sa.Column(sa.TEXT, nullable=False))
    birthdate: datetime.date = Field(sa_column=sa.Column(sa.Date), nullable=False)
    created_at: str = Field(sa_column=sa.Column(sa.DateTime(timezone=True), default=sa.func.now()))
