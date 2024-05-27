from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    name: str
    sex: str
    favProLang: str
    email: EmailStr

class UserResponse(BaseModel):
    id: int
    name: str
    sex: str
    favProLang: str
    email: EmailStr

    class Config:
        orm_mode = True
        from_attributes = True
