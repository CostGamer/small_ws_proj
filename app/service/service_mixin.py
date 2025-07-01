from app.repo import RoomRepo, UserRepo


class RoomServiceMixin:
    def __init__(self, room_repo: RoomRepo) -> None:
        self._room_repo = room_repo


class UserServiceMixin:
    def __init__(self, user_repo: UserRepo) -> None:
        self._user_repo = user_repo
