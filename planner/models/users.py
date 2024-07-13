"""
users.py: 사용자 처리용 모델을 정의
"""
from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from models.events import Event


class User(BaseModel):
    """
    email: 사용자 이메일
    password: 사용자 패스워드
    events: 해당 사용자가 생성한 이벤트. 처음에는 비어 있다
    """
    email: EmailStr = Field(...)
    password: str = Field(...)
    events: Optional[List[Event]] = Field(default=None)

    class Config: # 문서 출력 순서가 알파벳 순으로 정렬된다.
        json_schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "password": "strong!!!",
            }
        }


class UserSignIn(BaseModel):
    email: EmailStr
    password: str

    class Config:
        json_schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "password": "strong!!!"
            }
        }
