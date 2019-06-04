# Pull base image
FROM python:3.7-slim

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
RUN pip install pipenv

RUN apt-get update -y && \
    apt-get install -y curl unzip zip libc++-dev


RUN ls

RUN /bin/bash -c "curl https://dl.google.com/android/repository/build-tools_r28.0.2-linux.zip --output /tmp/download.zip"

RUN unzip /tmp/download.zip -d /tmp

RUN ls -la /tmp

RUN mv /tmp/android-9/aapt /bin/.

COPY . /code/

RUN python3 -m venv . && \
    ls -la

RUN /bin/bash -c "source bin/activate"

RUN pip install django djangorestframework

RUN cd rest-api-django/project && \
    ls && \
    python ./manage.py migrate && \
    python ./manage.py makemigrations androidPackageManager

# EXPOSE 8000
CMD ["python", "./rest-api-django/project/manage.py", "runserver", "0.0.0.0:8000"]