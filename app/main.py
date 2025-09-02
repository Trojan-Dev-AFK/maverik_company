# Entry point for FastAPI

from fastapi import FastAPI
from .exceptions import register_exception_handlers
from .middleware import RateLimitMiddleware
from .routers import items, auth
import os


app = FastAPI(title="Minimal FastAPI Application", version="1.0.0")


register_exception_handlers(app)


if not os.getenv("TESTING"):
    app.add_middleware(RateLimitMiddleware, limit=5, window_seconds=60)  # type: ignore


app.include_router(items.router, prefix="/items", tags=["items"])
app.include_router(auth.router, prefix="/auth", tags=["auth"])


@app.get("/health")
def health():
    return {"status": "ok"}
