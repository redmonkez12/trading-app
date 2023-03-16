from fastapi import APIRouter, Body, Response, status, Depends, HTTPException
import json

from app.auth.token import create_access_token
from app.auth.user import get_current_user
from app.controllers.users.ApiExamples import login_example, register_example, change_password_example
from app.deps import get_user_service
from app.exceptions.UserNotFoundException import UseNotFoundException
from app.models.User import User
from app.requests.users.ChangePassword import ChangePasswordRequest
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

        return Response(status_code=status.HTTP_200_OK,
                        content=json.dumps({"access_token": access_token, "token_type": "bearer"}))
    except UseNotFoundException as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e),
            headers={"WWW-Authenticate": "Bearer"},
        )
    except Exception as e:
        print(e)
        return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content="Something went wrong")


@user_router.post("/")
async def register(*, user_service: UserService = Depends(get_user_service),
                   request: RegisterRequest = Body(..., examples=register_example)):
    try:
        await user_service.register_user(request)
    except Exception:
        return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content="Something went wrong")

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@user_router.patch("/password")
async def change_password(*, user_service: UserService = Depends(get_user_service),
                          request: ChangePasswordRequest = Body(..., examples=change_password_example),
                          current_user: User = Depends(get_current_user)
                          ):
    try:
        await user_service.change_password(current_user, request)
    except UseNotFoundException as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"message": str(e), "code": "INVALID_PASSWORD", "status": status.HTTP_400_BAD_REQUEST, },
        )
    except Exception as e:
        print(e)
        return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content="Something went wrong")

    return Response(status_code=status.HTTP_204_NO_CONTENT)
