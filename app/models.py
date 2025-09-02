# Pydantic request & response models

from typing import Optional
from pydantic import BaseModel, Field


# Request Model
class ItemCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    price: float = Field(..., gt=0)  # type: ignore


# Response Model
class ItemResponse(ItemCreate):
    id: int


# (bonus) Auth models
class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=6)


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
