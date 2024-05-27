from sqlalchemy.orm import Session
from fastapi import Depends
from app.schemas.user import UserCreate, UserResponse
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.core.database import get_db

class UserService:
    def __init__(self, db: Session = Depends(get_db)):
        self.user_repository = UserRepository(db)

    async def create_user(self, user_create: UserCreate) -> UserResponse:
        user = self.user_repository.create_user(user_create)
        return UserResponse.from_orm(user)
