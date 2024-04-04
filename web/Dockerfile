FROM node:20-alpine

LABEL maintenair="Flash"

WORKDIR /app

COPY . .

RUN npm install && \
    npm run build

CMD ["npm","run","preview","--host"]