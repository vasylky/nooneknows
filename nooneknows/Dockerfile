FROM nginx:alpine

RUN rm -rf /usr/share/nginx/html/*

COPY frontend/index.html /usr/share/nginx/html/
COPY frontend/styles.css /usr/share/nginx/html/

EXPOSE 80
