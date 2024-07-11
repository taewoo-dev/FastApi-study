from fastapi import APIRouter, Path, HTTPException, status, Request, Depends
from fastapi.templating import Jinja2Templates
from starlette.templating import _TemplateResponse

from model import Todo, TodoItem, TodoItems

todo_router = APIRouter()

todo_list = []

templates = Jinja2Templates(directory="templates/")


@todo_router.post("/todo", status_code=201)
async def add_todo(request: Request, todo: Todo = Depends(Todo.as_form)) -> _TemplateResponse:
    todo.id = len(todo_list) + 1
    todo_list.append(todo)
    return templates.TemplateResponse("todo.html",
                                      {
                                          "request": request,
                                          "todos": todo_list
                                      })


@todo_router.get("/todo", response_model=TodoItems)
async def retrieve_todos(request: Request) -> _TemplateResponse:
    """
    get방식으로 todolist를 전부 보여주는 함수
    :return: TodoItems(응답 모델)
    """
    return templates.TemplateResponse("todo.html", {
        "request": request,
        "todos": todo_list
    })


@todo_router.get("/todo/{todo_id}")
async def get_single_todo(request: Request, todo_id: int = Path(..., title="The ID of the todo to retrieve.")) -> _TemplateResponse:
    """
    get방식으로 todolist를 하나씩 보여주는 함수
    :param request:
    :param todo_id: 기본 인자로 경로 매개변수인 Path 설정
    :return:
    """
    for todo in todo_list:
        if todo.id == todo_id:
            return templates.TemplateResponse("todo.html",{
                "request": request,
                "todo": todo
            })
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo with supplied ID doesn't exist"
    )


@todo_router.put("/todo/{todo_id}")
async def update_todo(todo_data: TodoItem, todo_id: int = Path(..., title="The ID of the todo to updated.")) -> dict:
    """
    put방식으로 원하는 id의 item속성을 변경하는 함수
    :param todo_data:
    :param todo_id:
    :return:
    """

    for todo in todo_list:
        if todo.id == todo_id:
            todo.item = todo_data.item
            return {
                "message": "Todo updated successfully"
            }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo with supplied ID doesn't exist"
    )


@todo_router.delete("/todo/{todo_id}")
def delete_single_todo(todo_id: int = Path(..., title="The ID of the todo to delete.")) -> dict:
    """

    :param todo_id:
    :return:
    """
    for index in range(len(todo_list)):
        todo = todo_list[index]
        if todo.id == todo_id:
            todo_list.pop(index)
            return {
                "message": "Todo deleted successfully"
            }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo with supplied ID doesn't exist"
    )


@todo_router.delete("/todo")
async def delete_all_todo() -> dict:
    todo_list.clear()
    return {
        "message": "Todo deleted all successfully!!."
    }
