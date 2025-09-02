# In-memory storage (dict)

from typing import Dict
from .models import ItemResponse, ItemCreate


# In-memory store
_items: Dict[int, ItemResponse] = {}
_next_id = 1


def create_item(data: ItemCreate) -> ItemResponse:
    global _next_id
    item = ItemResponse(id=_next_id, **data.model_dump())
    _items[_next_id] = item
    _next_id += 1
    return item


def get_item(item_id: int) -> ItemResponse | None:
    return _items.get(item_id)


def update_item(item_id: int, data: ItemCreate) -> ItemResponse | None:
    if item_id in _items:
        updated = ItemResponse(id=item_id, **data.model_dump())
        _items[item_id] = updated
        return updated
    return None


def delete_item(item_id: int) -> bool:
    return _items.pop(item_id, None) is not None


def list_items() -> list[ItemResponse]:
    return list(_items.values())
