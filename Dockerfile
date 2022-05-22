# production
FROM python:3.8-alpine

COPY . /app
RUN apk add gcc musl-dev && \
    pip install -r /app/requirements.txt
WORKDIR /app/recipes_app
CMD python manage.py runserver 0.0.0.0:8000
