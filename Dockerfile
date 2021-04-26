FROM node:latest as builder

WORKDIR /app

COPY package.json .

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

COPY ./ ./

RUN npm run build


FROM nginx
EXPOSE 80
COPY --from=builder /app/dist /usr/share/nginx/html