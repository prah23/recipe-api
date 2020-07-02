FROM python:3.8-alpine
MAINTAINER hpb1 

# The source on the copy command is the file(s) in the respository.
# The destination is docker image.

ENV PYTHONUNBUFFERED 1
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user
