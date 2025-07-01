from .service_mixin import UserServiceMixin
from app.models.pydantic import GetUser


class CreateUserService(UserServiceMixin):
    async def __call__(self, name: str) -> GetUser:
        return await self._user_repo.create_user(name=name)
