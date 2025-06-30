from datetime import datetime

from sqlalchemy import func, ForeignKey
from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .rooms import Room
    from .msg import Message


class User(Base):
    __tablename__ = "users"

    nickname: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    user_rooms: Mapped[list["UserRoom"]] = relationship(
        "UserRoom", back_populates="user"
    )


class UserRoom(Base):
    __tablename__ = "user_room"

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    room_id: Mapped[int] = mapped_column(ForeignKey("rooms.id"), nullable=False)

    user: Mapped["User"] = relationship("User", back_populates="user_rooms")
    room: Mapped["Room"] = relationship("Room", back_populates="user_rooms")
    message: Mapped["Message"] = relationship("Message", back_populates="user_room")
