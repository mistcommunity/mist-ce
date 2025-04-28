FROM nginx:1.27-alpine

RUN set -x \
	# && addgroup -g 82 -S www-data \
	&& adduser -u 82 -D -S -G www-data www-data

COPY ./static /srv/www/static

RUN wget -O novnc.tar.gz https://github.com/novnc/noVNC/archive/refs/tags/v1.6.0.tar.gz && \
	tar xvzf novnc.tar.gz && \
	rm novnc.tar.gz && \
	mv noVNC-1.6.0 /srv/www/static/novnc

COPY ./nginx.conf ./nginx-listen.conf /etc/nginx/
