FROM python:3.8.3-slim-buster
RUN apt-get update 
WORKDIR /web-app-docker
COPY requirments.txt requirments.txt
RUN pip install -r requirments.txt
RUN groupadd -g 999 webuser && \
    useradd -r -u 999 -g webuser webuser
USER webuser
COPY app.py /opt/app.py
ENTRYPOINT FLASK_APP=/opt/app.py flask run --host=0.0.0.0
