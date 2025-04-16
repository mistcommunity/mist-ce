FROM vault:1.13.3
RUN apk add vim grep socat jq
RUN wget -O /bin/wait-for https://github.com/eficode/wait-for/releases/download/v2.2.4/wait-for \
    && chmod +x /bin/wait-for
COPY ./init /init
COPY vault-start.sh /vault-start.sh
