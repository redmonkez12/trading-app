import datetime

from sqlmodel import SQLModel, Field

from app.models.User import User
import sqlalchemy as sa


class UserPassword(SQLModel, table=True):
    __tablename__ = "user_passwords"

    user_password_id: int = Field(default=True, primary_key=True)
    value: str = Field(sa_column=sa.Column(sa.TEXT, nullable=False))
    user_id: int = Field(sa_column=sa.Column(sa.Integer, sa.ForeignKey(User.user_id, ondelete="CASCADE")),
                         nullable=False)
    created_at: datetime.datetime = Field(sa_column=sa.Column(sa.DateTime(timezone=True), default=sa.func.now()))
