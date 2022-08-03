FROM python:3.9

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./src/requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY ./docker/run.sh /gunicorn_django/run.sh
RUN chmod +x /gunicorn_django/run.sh
WORKDIR /app

CMD /gunicorn_django/run.sh
