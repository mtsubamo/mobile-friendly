FROM python:3.5

COPY ./config.json /
COPY ./main.py /
COPY ./_search.py /
COPY ./_mobilefriendly.py /

RUN apt-get update && apt-get install vim -y
RUN pip install --upgrade google-api-python-client
