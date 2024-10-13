# Dockerfile for primary.py
FROM python:3.9-slim

WORKDIR /app

COPY primary.py .

RUN pip install requests

CMD ["python", "primary.py"]