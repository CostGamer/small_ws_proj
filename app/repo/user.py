from sqlalchemy import insert
from app.models.sql import User
from app.models.pydantic import GetUser
from .repo_mixin import RepoMixin


class UserRepo(RepoMixin):
    async def create_user(self, name: str) -> GetUser:
        query = insert(User).values(nickname=name).returning(User)
        result = (await self._con.execute(query)).scalar_one()
        return GetUser.model_validate(result, from_attributes=True)
