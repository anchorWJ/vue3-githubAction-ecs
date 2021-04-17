FROM tiangolo/uwsgi-nginx-flask:python3.8

COPY requirements.txt .
RUN pip install -r requirements.txt 
COPY .  /usr/src/app
WORKDIR /usr/src/app

ENTRYPOINT FLASK_APP=/usr/src/app/app.py flask run  -h 0.0.0.0  -p 80

RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y \
        build-essential -y \
        curl \
        nmap \
        git \
        nano \
    && rm -rf /var/lib/apt/lists/*



