# FastAPI Assignment


A minimal FastAPI app demonstrating CRUD, Pydantic models, custom exceptions, and rate limiting. Includes optional JWT auth and Dockerfile.


## Run locally
```bash
python -m venv .venv && source .venv/bin/activate # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open: http://127.0.0.1:8000/docs

## Endpoints

- POST /items/ – create item
- GET /items/{id} – read item
- PUT /items/{id} – update item
- DELETE /items/{id} – delete item
- GET /items/ – list items
- POST /auth/register – register
- POST /auth/login – login

## Rate Limiting

Global middleware: 5 requests / 60 seconds per IP. Exceeding returns 429 with { "detail": "Rate limit exceeded" }.

## Tests

Run below commands

```bash
cd maveric_item_price
$env:TESTING="1"
pytest -v
```

## Docker

```bash
docker build -t maveric_item_price .
docker run -p 8000:8000 maveric_item_price
```
