# Rate limiting middleware

import time
from collections import deque, defaultdict
from typing import Deque, Dict


from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse, Response


class RateLimitMiddleware(BaseHTTPMiddleware):

    def __init__(self, app, limit: int = 5, window_seconds: int = 60):
        super().__init__(app)
        self.limit = limit
        self.window = window_seconds
        self.hits: Dict[str, Deque[float]] = defaultdict(deque)

    async def dispatch(self, request: Request, call_next):
        # Extract client IP (respect X-Forwarded-For if present)
        client_ip = request.headers.get("x-forwarded-for")
        if client_ip:
            client_ip = client_ip.split(",")[0].strip()
        else:
            client_ip = request.client.host if request.client else "unknown"

        now = time.time()
        q = self.hits[client_ip]

        # Evict timestamps outside the window
        while q and (now - q[0]) > self.window:
            q.popleft()

        if len(q) >= self.limit:
            return JSONResponse(
                status_code=429, content={"detail": "Rate limit exceeded"}
            )

        q.append(now)
        response: Response = await call_next(request)
        return response
