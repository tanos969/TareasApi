FROM ubuntu:18.04

ENV DEBIAN_FRONTEND=noninteractive

# Upgrade system packages
RUN apt-get -y update && \
 apt-get -y upgrade && \
 apt-get -y dist-upgrade && \
 apt-get -y autoremove && \
apt-get clean 
 
# remove python2
RUN apt-get remove --purge python -y

# 2. Install Python3 and required libraries

RUN apt-get install -y python3-dev python3-tk python3-numpy libpython3-all-dev python3-pip libpython3-all-dev python3-all && \
 apt-get install -y libzbar0 && \
 apt install -y poppler-utils && pip3 install --upgrade pip

# Install runtime apt based dependencies
RUN apt-get install -y \
  bash-completion \
  tree \
  musl-dev \
  mc \
  curl \
  util-linux \
  libmysqlclient-dev

# Install buildtime apk based dependencies
RUN apt-get install -y build-essential \
  gcc \
  make \
  libc-dev \
  libffi-dev

# Install Python PIP dependencies
WORKDIR /tmp
COPY requirements.txt /tmp/
RUN pip install --upgrade pip && pip install -r requirements.txt
RUN pip install awscli

# Clean unused packages
#RUN apk del .build-deps
RUN rm -rf /tmp/* /var/tmp/*

# Define application resources
RUN mkdir -p /usr/src/api
COPY . /usr/src/api

# Define application volumes
# -

## Exposed ports
# Flask app
EXPOSE 8080

# Define base path for the application commands
WORKDIR /usr/src/api

# Default command
#CMD ["uwsgi", "--ini", "salami_score.ini"]
CMD ["python", "/usr/src/api/manage.py", "run"]

