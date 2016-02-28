FROM ubuntu:latest

MAINTAINER Abner Kang <abner.kang.dev@gmail.com>

RUN apt-get update && \
    apt-get install -y ncurses-base  ncurses-dev \ 
                       python \
                       python-dev \
                       python-pip \
                       build-essential \
    && apt-get clean \
    && apt-get autoclean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN mkdir -p /home/monitor

WORKDIR /home/monitor

ADD ./code /home/monitor/code
ADD ./misc /home/monitor/misc

RUN pip install -r /home/monitor/misc/requirement.txt

EXPOSE 5000

ENTRYPOINT ['python']

CMD ['./code/run.py', 'runserver', '--host 0.0.0.0']


