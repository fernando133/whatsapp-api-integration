# ./django-docker/app/Dockerfile
FROM python:3.7
# set work directory
WORKDIR /opt/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# install dependencies
RUN pip install --upgrade pip

COPY ./requirements.txt /opt/app/requirements.txt
RUN chmod +x /opt/app/requirements.txt
RUN pip install -r requirements.txt

RUN apt-get update -y
RUN apt-get install -y python3-dev
# copy project

# Install python dependencies in /.venv
COPY Pipfile /opt/app/

# Install the requirements to the container
RUN pip install pipenv
RUN pipenv install

COPY . /opt/app/
