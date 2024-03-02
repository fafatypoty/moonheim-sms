from pydantic import BaseModel


class Send(BaseModel):
    message_id: str
    status: str


class Status(BaseModel):
    message_id: str
    status_dlr: str
