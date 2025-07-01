from dishka import make_async_container

from .providers import (
    RepoProvider,
    ServiceProvider,
    SettingsProvider,
    DBProvider,
)

container = make_async_container(
    SettingsProvider(),
    DBProvider(),
    RepoProvider(),
    ServiceProvider(),
)
