FROM node:latest

RUN mkdir -p /var/www/app

WORKDIR /var/www/app

COPY ./client/vite ./var/www/app

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

RUN npm run build

EXPOSE 3000

ENTRYPOINT ["npm", "run", "serve"]
