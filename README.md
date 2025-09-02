# FastAPI Assignment


A minimal FastAPI app demonstrating CRUD, Pydantic models, custom exceptions, and rate limiting. Includes optional JWT auth and Dockerfile.


## Run locally
```bash
python -m venv .venv
source .venv/bin/activate # or .\.venv\scripts\activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Endpoints

Open -> http://127.0.0.1:8000/docs or http://127.0.0.1:8000/redoc

## Rate Limiting

Global middleware: 5 requests / 60 seconds per IP. Exceeding returns 429 with { "detail": "Rate limit exceeded" }.

## Tests

### Automatic

Run below commands

```bash
cd maverik_company
$env:TESTING="1"
pytest -v
```

### Manual

- Install API Dog -> https://apidog.com/download/.
- Import collection json present inside `apidog_collection` folder into the application.
- Make sure to add the access token (after using register and login endpoints) into the Auth section in collection folder settings.
- Execute all the available test cases.

## Docker

```bash
docker build -t maveric_item_price .
docker run -p 8000:8000 maveric_item_price
```
