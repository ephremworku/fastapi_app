from fastapi import APIRouter, Depends
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import UserService

router = APIRouter()

@router.post("/user", response_model=UserResponse)
async def create_user(user: UserCreate, user_service: UserService = Depends()):
    try:
        user_response = await user_service.create_user(user)
        return user_response.dict()
    except Exception as e:
        response = {"error": str(e)}  # Convert exception to string
        return response  