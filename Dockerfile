From python:3.10-alpine

RUN apk update && apk add --no-cache \
    gcc \
    musl-dev \
    postgresql-dev \
    libpq -dev./\
    python3-dev \
    build-base
WORKDIR /app

COPY requirement.txt /app/

RUN python -m venv venv

RUN . /venv/bin/activate

RUN pip install --upgrade pip && pip install -r requirement.txt

COPY . /app/

EXPOSE 8000

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]