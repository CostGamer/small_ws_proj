from fastapi import APIRouter
from dishka.integrations.fastapi import FromDishka, inject

from app.models.pydantic import GetUser
from app.service import CreateUserService

user_router = APIRouter(prefix="/user", tags=["user"])


@user_router.post(
    "",
    description="create user",
    response_model=GetUser,
)
@inject
async def create_user(
    name: str, create_user_ser: FromDishka[CreateUserService]
) -> GetUser:
    return await create_user_ser(name)
