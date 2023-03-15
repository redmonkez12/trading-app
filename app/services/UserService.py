from sqlmodel import Session

from app.models.User import User
from app.requests.users.Register import RegisterRequest


class UserService:
    def __init__(self, session: Session):
        self.session = session

    async def register_user(self, user: RegisterRequest):
        self.session.add(User(
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            birthdate=user.birthdate,
        ))
        self.session.commit()

    def login(self):
        pass

    def change_password(self):
        pass
