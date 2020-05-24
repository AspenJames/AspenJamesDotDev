FROM node:14-alpine

WORKDIR /app

COPY ./app/babel.config.json ./
COPY ./app/package.json      ./
RUN npm install

COPY ./app/render_server.js ./

COPY ./app/static/js/ssr ./app/static/js/ssr

CMD ["node", "render_server.js"]
