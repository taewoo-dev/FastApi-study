from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from typing import List
from database.connection import conn
from contextlib import asynccontextmanager

from routes.users import user_router
from routes.events import event_router

import uvicorn


@asynccontextmanager
async def lifespan(app: FastAPI):
    # 어플리케이션 시작
    conn()
    yield
    # 어플리케이션 종료
    print("어플리케이션을 종료합니다")


app = FastAPI(lifespan=lifespan)
# 라우트 등록
app.include_router(user_router, prefix="/user")
app.include_router(event_router, prefix="/event")


@app.get("/")
async def home():
    return RedirectResponse(url="/event/")


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
