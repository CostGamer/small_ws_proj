from sqlalchemy.ext.asyncio import AsyncSession


class RepoMixin:
    def __init__(self, con: AsyncSession) -> None:
        self._con = con
