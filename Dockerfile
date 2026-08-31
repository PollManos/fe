FROM python:3.12-slim

WORKSPACE /app

COPY . .

CMD ["python3","app.py"]
