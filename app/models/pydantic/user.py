from pydantic import BaseModel, ConfigDict


class GetUser(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    nickname: str
