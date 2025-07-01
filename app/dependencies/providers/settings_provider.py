from dishka import Provider, Scope, provide

from app.configs.settings import Settings


class SettingsProvider(Provider):
    @provide(scope=Scope.APP)
    async def get_settings(self) -> Settings:
        return Settings()
