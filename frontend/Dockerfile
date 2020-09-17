FROM node:latest
ENV HOST 0.0.0.0
RUN mkdir /frontend
WORKDIR /frontend
# Install dependencies
# COPY package.json yarn.lock /app/
# RUN npm install
# Add rest of the client code
# COPY . /frontend
COPY ./nuxt/dist /frontend/nuxt
COPY ./nuxt/package.json /frontend/nuxt
COPY ./nuxt/yarn.lock /frontend/nuxt
EXPOSE 3000