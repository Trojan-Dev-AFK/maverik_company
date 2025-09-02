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
- POST /auth/register – (bonus) register
- POST /auth/login – (bonus) login

## Rate Limiting

Global middleware: 5 requests / 60 seconds per IP. Exceeding returns 429 with { "detail": "Rate limit exceeded" }.

## Tests (manual)

Use the Swagger UI or curl examples:

```bash
curl -X POST http://127.0.0.1:8000/items/ \
-H 'Content-Type: application/json' \
-d '{"name":"Pen","price":1.5}'


curl http://127.0.0.1:8000/items/1


curl -X PUT http://127.0.0.1:8000/items/1 \
-H 'Content-Type: application/json' \
-d '{"name":"Blue Pen","price":2.0,"description":"Gel"}'


curl -X DELETE http://127.0.0.1:8000/items/1
```

## Tests (Automatic)

Run below commands

```bash
cd maveric_item_price
$env:TESTING="1"
pytest -v
```

## Docker (bonus)

```bash
docker build -t fastapi-assignment .
docker run -p 8000:8000 fastapi-assignment
```
