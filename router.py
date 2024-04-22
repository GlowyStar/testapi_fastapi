from typing import Annotated

from fastapi import APIRouter, Depends

from repository import TaskRepository
from schemas import STaskAdd, STask, STaskId

tasks = []

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"],
)


@router.post("")
async def add_task(
        task: Annotated[STaskAdd, Depends()],
) -> STaskId:
    task_id = await TaskRepository.add_one(task)
    return {"ok": True, "task_id": task_id}


@router.get("")
async def get_task() -> list[STask]:
    tasks = await TaskRepository.find_all()
    return {"data": tasks}  # FastAPI сам умеет конвертировать модели pydantic в JSON и возвращать их в ответ
