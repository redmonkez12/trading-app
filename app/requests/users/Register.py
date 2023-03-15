from pydantic import BaseModel, Field


class RegisterRequest(BaseModel):
    first_name: str = Field(description="The field first_name is mandatory")
    last_name: str = Field(description="The field last_name is mandatory")
    email: str = Field(description="The field email is mandatory")
    username: str = Field(description="The field username is mandatory")
    password: str = Field(description="The field password is mandatory")
    birthdate: str = Field(description="The field birthdate is mandatory")