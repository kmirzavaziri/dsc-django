FROM python:3.9.13-alpine3.16

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./src/requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

WORKDIR /app

ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH

CMD ["gunicorn", "--bind", ":8000", "--workers", "1", "main.wsgi:application"]
