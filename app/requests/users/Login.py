from pydantic import BaseModel, Field


class LoginRequest(BaseModel):
    email: str = Field(description="The field email is mandatory")
    password: str = Field(description="The field email is mandatory")
