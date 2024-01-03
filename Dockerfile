FROM python:3 AS development

ENV LANG C.UTF-8

RUN echo "PS1='\u@\h:\w\$ '" >> /root/.bashrc

ENV APP_HOME /var/service

# Set up libs needed for psycopg2
# https://www.psycopg.org/docs/install.html#build-prerequisites
# RUN apt-get install python3-dev libpq-dev

RUN mkdir -p $APP_HOME

ADD . $APP_HOME

WORKDIR $APP_HOME

RUN virtualenv .venv

RUN pip install poetry

RUN poetry install
