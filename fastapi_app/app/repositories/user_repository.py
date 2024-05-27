from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user_create: UserCreate) -> User:
        user = User(
            name=user_create.name,
            sex=user_create.sex,
            favProLang=user_create.favProLang,
            email=user_create.email
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
