FROM hub.kce.ksyun.com/ezone-public/python:3.9.6-alpine

RUN git config --global user.name "admin" \
    && git config --global user.email "admin@ezone.work" \
    && git config --global http.sslVerify false

COPY ./ /UITest

WORKDIR /UiTest