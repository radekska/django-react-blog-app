FROM node:13.12.0-alpine

WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

EXPOSE 3000

COPY package.json ./
COPY package-lock.json ./

RUN npm install && npm install react-router-dom \
    && npm install @material-ui/core \
    && npm i --save material-ui-search-bar \
    && npm install @material-ui/icons \
    && npm install axios

COPY . ./

CMD ["npm", "start"]