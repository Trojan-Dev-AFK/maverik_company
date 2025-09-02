# Bonus (register & login)

from fastapi import APIRouter, HTTPException
from ..models import UserCreate, TokenResponse
from ..security import hash_password, verify_password, create_access_token


router = APIRouter()


_users: dict[str, str] = {}


@router.post("/register", status_code=201)
def register(user: UserCreate):
    if user.username in _users:
        raise HTTPException(status_code=400, detail="Username already exists")
    _users[user.username] = hash_password(user.password)
    return {"message": "User registered"}


@router.post("/login", response_model=TokenResponse)
def login(user: UserCreate):
    hashed = _users.get(user.username)
    if not hashed or not verify_password(user.password, hashed):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token(subject=user.username)
    return TokenResponse(access_token=token)
