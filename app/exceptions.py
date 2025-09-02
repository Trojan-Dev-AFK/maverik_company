# Custom exception class & handlers

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse


class ItemNotFoundException(Exception):
    def __init__(self, item_id: int):
        self.item_id = item_id


def register_exception_handlers(app: FastAPI):
    @app.exception_handler(ItemNotFoundException)
    async def item_not_found_handler(request: Request, exc: ItemNotFoundException):
        return JSONResponse(
            status_code=404,
            content={"detail": f"Item with ID {exc.item_id} not found"},
        )
