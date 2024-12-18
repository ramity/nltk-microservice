FROM python:3.13-bookworm

WORKDIR /nltk

RUN pip install nltk
RUN pip install numpy
RUN pip install flask
RUN pip install requests
RUN pip install newspaper3k

COPY ./docker/nltk/init.bash /tmp/init.bash

ENTRYPOINT /tmp/init.bash
