from pydantic import BaseModel, ConfigDict


class GetUser(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    nickname: str


class GetUserRoom(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    user_id: int
    room_id: int
