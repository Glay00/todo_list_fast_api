from fastapi import APIRouter
from src.controller.todo import get_todo_controler

router = APIRouter()


@router.get("/lists/{list_id}/todos")
async def get_todos():
    return


@router.post("/lists/{list_id}/todos")
async def create_todo():
    return


@router.patch("/lists/{list_id}/todos/{todo_id}")
def update_todo():
    return


@router.delete("/lists/{list_id}/todos/{todo_id}")
def delete_todo():
    return
