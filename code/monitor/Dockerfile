FROM ubuntu:latest

MAINTAINER Abner Kang <abner.kang.dev@gmail.com>

RUN apt-get update && \
    apt-get install -y ncurses-base  ncurses-dev \ 
                       python-dev \
                       python-pip \
                       build-essential 

#RUN mkdir -p /home/monitor

#WORKDIR /home/monitor

#ADD ./code /home/monitor/code
#ADD ./misc /home/monitor/misc

#RUN pip install -r /home/monitor/misc/requirement.txt

EXPOSE 5000

# ENTRYPOINT ["python"]

# CMD ["python","./code/run.py", "runserver", "--host 0.0.0.0"]
CMD ["python", "--version"]

