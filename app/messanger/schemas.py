from pydantic import BaseModel
from datetime import datetime


class SMessanger(BaseModel):
    chat_id: int | None = None
    user_id: int | None = None
    bot_answers: str | None = None
    user_messages: str | None = None
    data: str | None = None
    date: datetime | None = None
