FROM python:latest

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /core
COPY . /core/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt