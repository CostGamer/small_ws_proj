from dishka import Provider, Scope, provide

from sqlalchemy.ext.asyncio import AsyncSession
from app.repo import RoomRepo, UserRepo


class RepoProvider(Provider):
    @provide(scope=Scope.REQUEST)
    async def get_room_repo(self, con: AsyncSession) -> RoomRepo:
        return RoomRepo(con)

    @provide(scope=Scope.REQUEST)
    async def get_user_repo(self, con: AsyncSession) -> UserRepo:
        return UserRepo(con)
