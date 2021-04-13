FROM python:3.8

RUN pip install Flask gunicorn

COPY src/ app/
WORKDIR /app

ENV PORT 8080