from fastapi import FastAPI, Depends

from contextlib import asynccontextmanager

from database import create_tables, delete_tables
from router import router as task_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Удаление таблиц")
    await delete_tables()
    print("Создание таблиц")
    await create_tables()
    print("Запуск работы")
    yield
    print("Завершение работы")


app = FastAPI(lifespan=lifespan)
app.include_router(task_router)