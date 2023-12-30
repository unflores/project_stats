FROM python:3 AS development

ENV LANG C.UTF-8

RUN echo "PS1='\u@\h:\w\$ '" >> /root/.bashrc

ENV APP_HOME /var/service

RUN mkdir -p $APP_HOME

ADD . $APP_HOME

WORKDIR $APP_HOME

RUN virtualenv .venv

RUN pip install poetry

RUN poetry install
