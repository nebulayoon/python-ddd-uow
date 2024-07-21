from fastapi import FastAPI
from app.api.v1.user_router import router
from contextlib import asynccontextmanager
import uvicorn

from app.db.connection import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(router, prefix="/api/v1", tags=["v1"])


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000)
