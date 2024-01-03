FROM python:3 AS development
# Server setup
ENV LANG C.UTF-8
RUN echo "PS1='\u@\h:\w\$ '" >> /root/.bashrc

RUN pip install --no-cache-dir --upgrade pip

# Application setup
ENV APP_HOME /var/service
RUN mkdir -p $APP_HOME
ADD . $APP_HOME

WORKDIR $APP_HOME

RUN pip install poetry

RUN poetry install
