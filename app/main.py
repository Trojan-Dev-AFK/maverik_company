# Entry point for FastAPI

from fastapi import FastAPI
from .exceptions import register_exception_handlers
from .middleware import RateLimitMiddleware
from .routers import items, auth


app = FastAPI(title="FastAPI Assignment", version="1.0.0")


# Register custom exception handlers
register_exception_handlers(app)


# Rate limiting middleware: 5 req / 60s per IP
app.add_middleware(RateLimitMiddleware, limit=5, window_seconds=60)  # type: ignore


# Routers
app.include_router(items.router, prefix="/items", tags=["items"])
app.include_router(auth.router, prefix="/auth", tags=["auth"])  # bonus


@app.get("/health")
def health():
    return {"status": "ok"}
