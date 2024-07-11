from fastapi import FastAPI, Request
from todo import todo_router
from fastapi.templating import Jinja2Templates
from starlette.templating import _TemplateResponse

app = FastAPI()

templates = Jinja2Templates(directory="templates/")


@app.get("/")
async def welcome(request: Request) -> _TemplateResponse:
    return templates.TemplateResponse("home.html",
                                      {
                                          "request": request,
                                          "message": "hello"
                                      })


app.include_router(todo_router)
