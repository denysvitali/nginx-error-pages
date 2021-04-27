FROM nginx:stable-alpine
ADD ./snippets /etc/nginx
RUN sed -i 's@include snippets/@include @' /etc/nginx/error_pages.conf
COPY ./conf/docker-nginx.conf /etc/nginx/conf.d/default.conf
COPY . /srv/http/default/
