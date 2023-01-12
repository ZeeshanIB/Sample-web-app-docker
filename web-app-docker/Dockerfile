FROM python:3.12.0a3-slim-bullseye
RUN apt-get update
RUN pip install flask
RUN groupadd -g 999 webuser && \
    useradd -r -u 999 -g webuser webuser
USER webuser
COPY ./app.py /opt/app.py
WORKDIR /opt
ENTRYPOINT FLASK_APP=/opt/app.py flask run --host=0.0.0.0
