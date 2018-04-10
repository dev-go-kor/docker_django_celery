FROM ubuntu:18.04

MAINTAINER DEV-GO

RUN apt-get update -y && \
    apt-get install -y \
    nginx \
    python3-dev \
    python3-pip

RUN pip3 install django uwsgi

RUN echo "daemon off;" >> /etc/nginx/nginx.conf
RUN rm -rf /etc/nginx/sites-enabled/default
COPY mysite_nginx.conf /etc/nginx/sites-enabled/mysite_nginx.conf

#COPY . /mysite/
VOLUME /mysite/
WORKDIR /mysite/

#RUN chmod +x /mysite/docker_start.sh
#CMD /mysite/docker_start.sh

EXPOSE 80