FROM python:slim

WORKDIR /django-backend

# If running by docker compose, there is no need to copy project files to
# django_backend folder as those are being mounted via volume.
# COPY . /django_backend
COPY requirements.txt /django-backend

RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]