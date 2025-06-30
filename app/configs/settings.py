from os import environ as env
from pathlib import Path
from pydantic import BaseModel, Field


def load_dotenv(path: str | Path) -> None:
    path = Path(path)
    if not path.exists():
        return
    with path.open(mode="r", encoding="utf-8") as file:
        for line in file:
            if line.startswith("#") or line.strip() == "":
                continue
            try:
                key, value = line.strip().split("=", maxsplit=1)
                value = value.strip().strip("''")
                env.setdefault(key, value)
            except ValueError:
                print(f"Invalid line in .env file: {line.strip()}")


load_dotenv(".env")


class PostgresSettings(BaseModel):
    host: str = Field(default="localhost", alias="POSTGRES_HOST")
    port: int = Field(default=5432, alias="POSTGRES_PORT")
    user: str = Field(default="user", alias="POSTGRES_USER")
    password: str = Field(default="my_password", alias="POSTGRES_PASSWORD")
    db_name: str = Field(default="my_database", alias="POSTGRES_DB")
    pool_size: int = Field(default=500, alias="DB_POOL_SIZE")
    max_overflow: int = Field(default=500, alias="DB_MAX_OVERFLOW")

    @property
    def db_uri(self) -> str:
        return f"postgresql+psycopg://{self.user}:{self.password}@{self.host}:{self.port}/{self.db_name}"


class Settings(BaseModel):
    database: PostgresSettings = Field(default_factory=lambda: PostgresSettings(**env))  # type: ignore
