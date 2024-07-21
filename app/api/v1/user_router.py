from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from app.db.connection import get_connection
from app.service_layers.uow.unit_of_work import PostgresUnitOfWork, UnitOfWork
from app.service_layers.user_service import UserService

router = APIRouter()


class UserCreateRequest(BaseModel):
    user_id: str
    name: str
    email: str


# DI를 위한 설정
def get_uow():
    connection = get_connection()
    return PostgresUnitOfWork(connection)


@router.post("/register")
async def register_user(request: UserCreateRequest, uow: UnitOfWork = Depends(get_uow)):
    user_service = UserService(uow)
    try:
        user_service.register_user(request.user_id, request.name, request.email)
        return {"message": "User registered successfully"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
