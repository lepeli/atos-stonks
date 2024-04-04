FROM node:20-alpine

LABEL maintenair="Flash"

WORKDIR /app

COPY . .

RUN npm install

RUN npm run build

CMD ["npm","run","preview","--host"]

EXPOSE 4173