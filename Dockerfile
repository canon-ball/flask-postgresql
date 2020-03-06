FROM ubuntu:latest
MAINTAINER Belkin Anton
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential python3.6
COPY . /temperature
WORKDIR /temperature
RUN pip3 install -r requirements.txt
EXPOSE 5000
CMD ["/usr/bin/python3.6", "start.py"]
