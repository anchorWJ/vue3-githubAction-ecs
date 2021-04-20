FROM node:latest

RUN mkdir -p /var/www/app

WORKDIR /var/www/app

COPY ./client/vite /var/www/app

RUN npm run build

EXPOSE 3000

ENTRYPOINT ["npm", "run", "serve"]
