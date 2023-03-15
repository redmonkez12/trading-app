from sqlmodel import Session, select

from app.auth.password import verify_password, get_password_hash
from app.exceptions.UserNotFoundException import UseNotFoundException
from app.models.User import User
from app.models.UserPassword import UserPassword
from app.requests.users.Login import LoginRequest
from app.requests.users.Register import RegisterRequest


class UserService:
    def __init__(self, session: Session):
        self.session = session

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
        query = (
            select(User.user_id, User.username, User.email, UserPassword.value.label("password"))
            .join(UserPassword)
            .where(User.username == data.username)
            .limit(1)
        )

        query_result = await self.session.execute(query)
        user: list[User] = query_result.first()

        if not user:
            raise UseNotFoundException("Username or password is invalid")

        if not verify_password(data.password, user.password):
            raise UseNotFoundException("Username or password is invalid")

        return user

    def change_password(self):
        pass
