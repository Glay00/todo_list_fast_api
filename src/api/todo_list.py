from fastapi import APIRouter, Depends
from pydantic import UUID4

from src.controller.todo import get_todo_controler, TodoController
from src.schemas.todo import TodoListResponse, TodoListRequest

router = APIRouter()


@router.get(
    "/lists",
    response_model=list[TodoListResponse],
    status_code=200,
)
async def get_list(
        todo_controller: TodoController = Depends(get_todo_controler),
) -> list[TodoListResponse]:
    result = await todo_controller.get_lists()
    return result


@router.post("/lists", status_code=201, )
async def create_list(
        todo_request: TodoListRequest,
        todo_controller: TodoController = Depends(get_todo_controler),
):
    result = await todo_controller.create_lists(todo_request.title)
    return result


@router.delete("/lists/{list_id}", status_code=204)
async def delete_list(
        list_id: UUID4,
        todo_controller: TodoController = Depends(get_todo_controler),
):
    await todo_controller.delete_list_id(list_id)
