# CRUD operation functions

from .models import ItemCreate, ItemResponse
from .exceptions import ItemNotFoundException
from . import database


def create_item(data: ItemCreate) -> ItemResponse:
    return database.create_item(data)


def read_item(item_id: int) -> ItemResponse:
    item = database.get_item(item_id)
    if not item:
        raise ItemNotFoundException(item_id)
    return item


def update_item(item_id: int, data: ItemCreate) -> ItemResponse:
    updated = database.update_item(item_id, data)
    if not updated:
        raise ItemNotFoundException(item_id)
    return updated


def delete_item(item_id: int) -> None:
    deleted = database.delete_item(item_id)
    if not deleted:
        raise ItemNotFoundException(item_id)


def list_items() -> list[ItemResponse]:
    return database.list_items()
