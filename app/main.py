from fastapi import FastAPI
from dishka.integrations.fastapi import setup_dishka

from app.dependencies.container import container
from app.handlers import room_router, user_router


def init_routers(app: FastAPI) -> None:
    app.include_router(room_router)
    app.include_router(user_router)


def setup_app() -> FastAPI:
    app = FastAPI(
        title="small WS project",
    )
    setup_dishka(app=app, container=container)
    init_routers(app)
    return app
