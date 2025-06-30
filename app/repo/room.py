from sqlalchemy.ext.asyncio import AsyncSession


class RoomRepo:
    def __init__(self, con: AsyncSession) -> None:
        self._con = con

    # async def create_room(self, )
