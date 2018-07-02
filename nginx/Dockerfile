FROM nginx:alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY ./sites-enabled/nginx.conf /etc/nginx/conf.d/default.conf