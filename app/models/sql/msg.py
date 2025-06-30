from datetime import datetime
from sqlalchemy import ForeignKey, func
from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .users import UserRoom


class Message(Base):
    __tablename__ = "message"

    user_room_id: Mapped[int] = mapped_column(
        ForeignKey("user_room.id"), nullable=False
    )
    message: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        nullable=False, server_default=func.now()
    )

    user_rooms: Mapped["UserRoom"] = relationship("UserRoom", back_populates="message")
