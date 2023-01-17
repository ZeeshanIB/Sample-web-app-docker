FROM python:3.8.3-slim-buster
RUN apt-get update 
RUN pip install psycopg2-binary
RUN pip install flask
RUN groupadd -g 999 webuser && \
    useradd -r -u 999 -g webuser webuser
USER webuser
COPY web-app-docker/app.py /opt/app.py
ENTRYPOINT FLASK_APP=/opt/app.py flask run --host=0.0.0.0
