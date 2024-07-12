from pydantic import BaseModel, Field
from typing import List, Optional
from fastapi import Form


class Todo(BaseModel):
    """
    요청 바디를 검증하는 클래스

    :param id,item : 클래스 변수로 타입힌팅과 함께 선언, None값이 할당되어있다
    """
    id: Optional[int] = Field(default=None) # Field를 None으로 선언해줘야 문제가 발생하지 않는다
    item: str

    @classmethod
    def as_form(
            cls,
            item: str = Form(...)
    ):
        return cls(item=item)

    class Config:
        """
        중첩 모델 (?) 왜 예시가 생기지 않을까
        """
        json_schema_extra = {
            "example": {
                "id": 1,
                "item": "Example Schema!"
            }
        }


class TodoItem(BaseModel):
    """
    todoitem 클래스이다.
    """
    item: str

    class Config:
        json_schema_extra = {
            "example": {
                "item": "Read the next chapter of the book"
            }
        }


class TodoItems(BaseModel):
    """
    사용자의 요청으로부터 데이터를 정제하여 원하는 필드(변수)만 반환하는 클래스(필터 모델)

    : Todo 클래스의 경우 id와 item 두가지 필드를 가지고 있다
    하지만 TodoItems 클래스를 이용하면 아래와 같이 item 필드만 보여준다
    """
    todos: List[TodoItem]

    class Config:
        json_schema_extra = {
            "example": {
                "todos": [
                    {
                        "items": "Example schema 1!"
                    },
                    {
                        "itme": "Example schema 2!"
                    }
                ]
            }
        }
