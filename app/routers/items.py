# Item-related routes

from app.security import get_current_user
from fastapi import APIRouter, Depends
from ..models import ItemCreate, ItemResponse
from .. import crud


router = APIRouter()


@router.post("/", response_model=ItemResponse, status_code=201)
def create_item(payload: ItemCreate, user: str = Depends(get_current_user)):
    return crud.create_item(payload)


@router.get("/{item_id}", response_model=ItemResponse)
def get_item(item_id: int, user: str = Depends(get_current_user)):
    return crud.read_item(item_id)


@router.put("/{item_id}", response_model=ItemResponse)
def update_item(
    item_id: int, payload: ItemCreate, user: str = Depends(get_current_user)
):
    return crud.update_item(item_id, payload)


@router.delete("/{item_id}")
def delete_item(item_id: int, user: str = Depends(get_current_user)):
    crud.delete_item(item_id)
    return {"message": "Item deleted"}


@router.get("/", response_model=list[ItemResponse])
def get_all_items(user: str = Depends(get_current_user)):
    return crud.list_items()
