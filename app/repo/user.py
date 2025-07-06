from sqlalchemy import insert, select
from app.models.sql import User, UserRoom, Room
from app.models.pydantic import GetUser, GetUserRoom
from .repo_mixin import RepoMixin


class UserRepo(RepoMixin):
    async def create_user(self, name: str) -> GetUser:
        query = insert(User).values(nickname=name).returning(User)
        result = (await self._con.execute(query)).scalar_one()
        return GetUser.model_validate(result, from_attributes=True)


class UserRoomRepo(RepoMixin):
    """Without validation"""
    async def bind_user_and_room(self, username: str, room_name: str) -> GetUserRoom | None:
        query = insert(UserRoom).values(
            user_id=select(User).where(User.nickname==username).scalar_subquery(),
            room_id=select(Room).where(Room.name==room_name).scalar_subquery()
        ).returning(UserRoom)
        result = (await self._con.execute(query)).scalar_one_or_none()
        return GetUserRoom.model_validate(result, from_attributes=True) if result else None

    async def check_user_in_room(self, username: str) -> list[str]:
        """Without validation"""
        query = select(Room.name).join(UserRoom).join(User).where(User.nickname==username)
        result = (await self._con.execute(query)).scalars().all()
        return [rooms for rooms in result]
