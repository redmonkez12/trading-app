from pydantic import BaseModel, Field


class LoginRequest(BaseModel):
    username: str = Field(description="The field username is mandatory")
    password: str = Field(description="The field password is mandatory")
