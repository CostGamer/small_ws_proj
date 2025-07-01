from fastapi import APIRouter
from dishka.integrations.fastapi import FromDishka, inject

from app.models.pydantic import GetRoom
from app.service import CreateRoomService, GetAllRoomsService

room_router = APIRouter(prefix="/room", tags=["room"])


@room_router.post(
    "",
    description="create room",
    response_model=GetRoom,
)
@inject
async def create_room(
    name: str, create_room_ser: FromDishka[CreateRoomService]
) -> GetRoom:
    return await create_room_ser(name)


@room_router.get(
    "/all",
    description="get all rooms",
    response_model=list[GetRoom],
)
@inject
async def get_all_rooms(
    get_all_rooms_ser: FromDishka[GetAllRoomsService],
) -> list[GetRoom]:
    return await get_all_rooms_ser()
