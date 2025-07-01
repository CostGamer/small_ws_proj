from sqlalchemy import insert, select
from app.models.sql import Room
from app.models.pydantic import GetRoom
from .repo_mixin import RepoMixin


class RoomRepo(RepoMixin):
    async def create_room(self, name: str) -> GetRoom:
        query = insert(Room).values(name=name).returning(Room)
        result = (await self._con.execute(query)).scalar_one()
        return GetRoom.model_validate(result, from_attributes=True)

    async def get_all_rooms(
        self,
    ) -> list[GetRoom]:
        query = select(Room)
        result = (await self._con.execute(query)).scalars().all()
        return [GetRoom.model_validate(res, from_attributes=True) for res in result]
