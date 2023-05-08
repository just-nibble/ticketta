FROM python:3.10-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ADD ./requirements.txt /app/requirements.txt

ADD . /app
WORKDIR /app

RUN pip install -r /app/requirements.txt

COPY ./entrypoint.sh /app/entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["sh", "/app/entrypoint.sh"]

