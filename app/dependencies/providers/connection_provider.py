from collections.abc import AsyncIterator
from dishka import Provider, Scope, provide
from sqlalchemy.ext.asyncio import AsyncSession

from app.configs.db import DatabaseConnection
from app.configs.settings import Settings


class DBProvider(Provider):
    @provide(scope=Scope.APP)
    async def get_db(self, settings: Settings) -> DatabaseConnection:
        return DatabaseConnection(settings)

    @provide(scope=Scope.APP)
    async def get_db_session(
        self, database: DatabaseConnection
    ) -> AsyncIterator[AsyncSession]:
        async with database.get_session() as session:
            yield session
