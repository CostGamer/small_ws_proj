from dishka import Provider, Scope, provide

from app.service import GetAllRoomsService, CreateUserService, CreateRoomService
from app.repo import RoomRepo, UserRepo


class ServiceProvider(Provider):
    @provide(scope=Scope.REQUEST)
    async def get_all_rooms_ser(self, room_repo: RoomRepo) -> GetAllRoomsService:
        return GetAllRoomsService(room_repo)

    @provide(scope=Scope.REQUEST)
    async def create_room_ser(self, room_repo: RoomRepo) -> CreateRoomService:
        return CreateRoomService(room_repo)

    @provide(scope=Scope.REQUEST)
    async def create_user_ser(self, user_repo: UserRepo) -> CreateUserService:
        return CreateUserService(user_repo)
