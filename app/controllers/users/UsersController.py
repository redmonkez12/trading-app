from fastapi import APIRouter, Body, Response, status, Depends, HTTPException
import json

from app.auth.token import create_access_token
from app.controllers.users.ApiExamples import login_example, register_example
from app.deps import get_user_service
from app.exceptions.UserNotFoundException import UseNotFoundException
from app.requests.users.Login import LoginRequest
from app.requests.users.Register import RegisterRequest
from app.services.UserService import UserService

user_router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@user_router.post("/login")
async def login(*, user_service: UserService = Depends(get_user_service),
                request: LoginRequest = Body(..., examples=login_example)):
    try:
        user = await user_service.login(request)

        access_token = create_access_token(
            data={"sub": user.username}
        )

        return Response(status_code=status.HTTP_200_OK, content=json.dumps({"access_token": access_token, "token_type": "bearer"}))
    except UseNotFoundException as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=e,
            headers={"WWW-Authenticate": "Bearer"},
        )
    except Exception as e:
        print(e)
        return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content="Something went wrong login")


@user_router.post("/")
async def register(*, user_service: UserService = Depends(get_user_service),
                   request: RegisterRequest = Body(..., examples=register_example)):
    try:
        await user_service.register_user(request)
    except Exception:
        return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content="Something went wrong register")

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@user_router.patch("/password")
async def change_password():
    pass
