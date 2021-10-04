FROM node:alpine

WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

COPY package.json ./

COPY package-lock.json ./

RUN npm install

RUN npm install react-router-dom && npm install @material-ui/core \
    && npm install axios

EXPOSE 3000

COPY ../.. ./

CMD ["npm", "start"]

