from fastapi import APIRouter, Body, Response, status, Depends

from app.controllers.users.ApiExamples import login_example, register_example
from app.deps import get_user_service
from app.requests.users.Login import LoginRequest
from app.requests.users.Register import RegisterRequest
from app.services.UserService import UserService

user_router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@user_router.post("/login")
async def login(request: LoginRequest = Body(..., examples=login_example)):
    print(request)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@user_router.post("/")
async def register(*, user_service: UserService = Depends(get_user_service),
                   request: RegisterRequest = Body(..., examples=register_example)):
    await user_service.register_user(request)

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@user_router.patch("/password")
async def change_password():
    pass
