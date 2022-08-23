FROM python:3.8

LABEL Author="neznajkin"

ENV PYTHONBUFFERED 1

WORKDIR /code
COPY . /code

RUN pip install -r requirements.txt