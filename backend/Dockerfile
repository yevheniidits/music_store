FROM python:3.10-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code
COPY requirements.txt /code/

RUN pip install -r /code/requirements.txt --no-cache-dir

COPY . /code/

EXPOSE 8000
