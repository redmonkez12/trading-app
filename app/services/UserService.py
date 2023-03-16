from sqlmodel import Session, select, update

from app.auth.password import verify_password, get_password_hash
from app.exceptions.UserNotFoundException import UseNotFoundException
from app.models.User import User
from app.models.UserPassword import UserPassword
from app.requests.users.ChangePassword import ChangePasswordRequest
from app.requests.users.Login import LoginRequest
from app.requests.users.Register import RegisterRequest


class UserService:
    def __init__(self, session: Session):
        self.session = session

    async def get_by_username(self, username: str):
        query = (
            select(User.user_id, User.username, User.email, UserPassword.value.label("password"))
            .join(UserPassword)
            .where(User.username == username)
            .limit(1)
        )

        result = await self.session.execute(query)
        return result.first()

    async def register_user(self, user: RegisterRequest):
        new_user = User(
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            birthdate=user.birthdate,
            username=user.username,
            passwords=[UserPassword(value=get_password_hash(user.password))]
        )

        self.session.add(new_user)
        await self.session.commit()

    async def login(self, data: LoginRequest):
        user = await self.get_by_username(data.username)

        if not user:
            raise UseNotFoundException("Username or password is invalid")

        if not verify_password(data.password, user.password):
            raise UseNotFoundException("Username or password is invalid")

        return user

    async def change_password(self, user: User, request_data: ChangePasswordRequest):
        if not verify_password(request_data.old_password, user.password):
            raise UseNotFoundException("Password is invalid")

        query = (
            select(UserPassword)
            .where(UserPassword.user_id == user.user_id)
            .limit(1)
        )

        data = await self.session.execute(query)
        user_password = data.scalars().first()

        user_password.value = get_password_hash(request_data.new_password)

        await self.session.commit()
