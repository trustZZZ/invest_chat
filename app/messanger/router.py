from fastapi import WebSocket, WebSocketDisconnect, APIRouter, Depends

from app.messanger.dao import MessagesDAO
from app.users.dependencies import get_current_user
from app.users.models import Users

router = APIRouter(
    prefix='/chat',
    tags=["Chat"]
)


class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    @staticmethod
    async def send_personal_message(message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        await MessagesDAO.add(message=message)
        for connection in self.active_connections:
            await connection.send_text(message)


manager = ConnectionManager()


@router.get("/messages")
async def get_messages(user: Users = Depends(get_current_user)):
    return await MessagesDAO.get_messages(user_id=user.id)


@router.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        # await manager.send_personal_message(f"Hello", websocket)
        while True:
            await manager.send_personal_message("Какой объект вы ищите?", websocket=websocket)
            data = await websocket.receive_text()
            await manager.send_personal_message(data, websocket)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        # await manager.broadcast(f"Client #{client_id} left the chat")
