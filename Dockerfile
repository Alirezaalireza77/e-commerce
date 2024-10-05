From python:3.10-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apk update && apk add --no-catch \
    gcc \
    musl-dev \
    postgresql-dev \
    libpq \
WORKDIR /app

COPY requrement.txt /app/

RUN pip install --upgrade pip && pip install -r requrement.txt

COPY . /app/

EXPOSE 8000
CMD [ "python", "manage.py", "runserver", "127.0.0.1:8000" ]