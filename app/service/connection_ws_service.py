from fastapi import WebSocket
from app.repo import UserRoomRepo

class WSConnectionService:
    def __init__(self, user_room_repo: UserRoomRepo):
        self.active_connections: dict[str, WebSocket] = {}
        self.room_users: dict[str, list[str]] = {}
        self._user_room_repo = user_room_repo
    
    async def connect(self, ws: WebSocket, username: str, room_name: str) -> bool:
        await ws.accept()

        if username in self.active_connections:
            old_ws = self.active_connections[username]
            await old_ws.close()
        self.active_connections[username] = ws

        user_rooms = set(await self._user_room_repo.check_user_in_room(username))
        if room_name in user_rooms:
            self._add_user_to_room(username, room_name)
            return True

        binded_user_room = await self._user_room_repo.bind_user_and_room(username, room_name)
        if not binded_user_room:
            await ws.close(code=4004, reason="Cannot join room")
            del self.active_connections[username]
            return False
        
        self._add_user_to_room(username, room_name)
        return True
    
    def _add_user_to_room(self, username: str, room_name: str):
        if room_name not in self.room_users:
            self.room_users[room_name] = []
        
        if username not in self.room_users[room_name]:
            self.room_users[room_name].append(username)
