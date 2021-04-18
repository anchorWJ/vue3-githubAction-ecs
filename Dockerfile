FROM node:latest

COPY ./client/vite /app
WORKDIR /app


ENV DEBCONF_NOWARNINGS yes
RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y \
        build-essential -y \
        curl \
        nmap \
        git \
        nano \
    && rm -rf /var/lib/apt/lists/*

RUN npm install

EXPOSE 5000

CMD ["npm", "run", "dev"]