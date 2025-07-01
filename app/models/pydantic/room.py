from datetime import datetime
from pydantic import BaseModel, ConfigDict


class GetRoom(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    created_at: datetime
