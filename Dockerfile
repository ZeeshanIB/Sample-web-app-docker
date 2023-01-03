FROM python:3.12.0a3-slim-bullseye
RUN apt-get update

RUN apt-get install -y python3-pip
RUN pip install flask
COPY app.py /opt/app.py
ENTRYPOINT FLASK_APP=/opt/app.py flask run --host=0.0.0.0
