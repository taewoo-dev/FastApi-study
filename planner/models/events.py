"""
events.py: 이벤트 처리용 모델을 정의
"""
from pydantic import BaseModel
from typing import List


class Event(BaseModel):
    """
    id: 자동 생성되는 고유 식별자
    title: 이벤트 타이틀
    image: 이벤트 이미지 배너의 링크
    description: 이벤트 설명
    tags: 그룹화를 위한 이벤트 태그
    location: 이벤트 위치
    """
    id: int
    title: str
    image: str
    description: str
    tags: List[str]
    location: str

    class Config:
        json_schema_extra = {
            "example": {
                "title": "FastAPI Book Launch",
                "image": "None",
                "description": "We will be discussing the contents of the FastApi Event",
                "tags": ["python","fastapi","book","launch"],
                "location": "Google Meet"
            }
        }