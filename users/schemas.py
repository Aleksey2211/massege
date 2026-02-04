from pydantic import BaseModel
from typing import Optional
from users.models import GenderEnum


class SUser(BaseModel):
    user_id: int
    email: str
    username: str
    surname: Optional[str] = None
    password: str
    gender: Optional[GenderEnum] = None
    user_image: Optional[str] = None