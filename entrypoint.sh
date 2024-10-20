alembic upgrade head
uvicorn src.main:app --root-path "/services" --host 0.0.0.0 --port $1