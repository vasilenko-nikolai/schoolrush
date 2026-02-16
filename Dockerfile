FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN alembic upgrade head

CMD ["python", "-m", "app.apps.server.app"]
