FROM python:3.10-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /app
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "deploy.app:app"]
