from pydantic import BaseModel

class Todo(BaseModel):
    """
    요청 바디를 검증하는 클래스
    """
    id: int
    item: str

    class Config:
        '''
        중첩 모델 (?) 왜 예시가 생기지 않을까
        '''
        schema_extra = {
            "example": {
                "id": 1,
                "item": "Example Schema!"
            }
        }
