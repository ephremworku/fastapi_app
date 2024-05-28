from fastapi import APIRouter, Depends
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import UserService
from fastapi.responses import FileResponse
router = APIRouter()

@router.post("/user", response_model=UserResponse)
async def create_user(user: UserCreate, user_service: UserService = Depends()):
    print('hell')
    try:
        user_response = await user_service.create_user(user)
        return user_response.dict()
    except Exception as e:
        response = {"error": "str(e)"}  # Convert exception to string
        return response  
@router.get("/register")
async def get_users():
    html_file_path = "static/index.html"
    return FileResponse(html_file_path)
@router.get("/register/success")
async def get_register_success():
    html_file_path = "static/success.html"
    return FileResponse(html_file_path)