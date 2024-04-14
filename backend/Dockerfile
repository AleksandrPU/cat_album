FROM python:3.11-alpine

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install -U pip --no-cache-dir && pip install -r requirements.txt --no-cache-dir

COPY . .

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "kittygram_backend.wsgi"]
