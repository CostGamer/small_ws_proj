from .service_mixin import RoomServiceMixin
from app.models.pydantic import GetRoom


class CreateRoomService(RoomServiceMixin):
    async def __call__(self, name: str) -> GetRoom:
        return await self._room_repo.create_room(name=name)


class GetAllRoomsService(RoomServiceMixin):
    async def __call__(
        self,
    ) -> list[GetRoom]:
        return await self._room_repo.get_all_rooms()
