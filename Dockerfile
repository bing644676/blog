FROM node:10
COPY ./ /app
WORKDIR /app
RUN npm install && npm run build

FROM nginx:1.15.2-alpine
RUN mkdir /app
COPY --from=0 /app/dist /app
COPY nginx.conf /etc/nginx/nginx.conf