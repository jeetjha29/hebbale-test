#Accommodations - Dockerfile
FROM python:3.8.16-slim-buster

RUN apt-get update

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000

CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000