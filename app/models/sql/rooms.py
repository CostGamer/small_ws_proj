from datetime import datetime
from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import func
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .users import UserRoom


class Room(Base):
    __tablename__ = "rooms"

    name: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    user_room: Mapped[list["UserRoom"]] = relationship(
        "UserRoom", back_populates="room"
    )
