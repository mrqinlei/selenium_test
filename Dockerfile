FROM python:3.7-alpine3.15

# 基础环境
RUN set -x && \
    sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories && \
    apk add bash tzdata ttf-dejavu zip busybox-extras curl tcpdump gcc g++ make libffi-dev openssl-dev libtool && \
    mkdir -p /app /app/logs /app/data && \
    echo "Asia/Shanghai" > /etc/timezone && \
    ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    rm -rf /var/cache/apk/*

#Java
RUN { \
		echo '#!/bin/sh'; \
		echo 'set -e'; \
		echo; \
		echo 'dirname "$(dirname "$(readlink -f "$(which javac || which java)")")"'; \
	} > /usr/local/bin/docker-java-home \
	&& chmod +x /usr/local/bin/docker-java-home
ENV JAVA_HOME /usr/lib/jvm/java-1.8-openjdk/jre
ENV PATH $PATH:/usr/lib/jvm/java-1.8-openjdk/jre/bin:/usr/lib/jvm/java-1.8-openjdk/bin

ENV JAVA_VERSION 8u302
ENV JAVA_ALPINE_VERSION 8.302.08-r2

RUN set -x \
	&& apk add --no-cache \
		openjdk8-jre="$JAVA_ALPINE_VERSION" \
	&& [ "$JAVA_HOME" = "$(docker-java-home)" ]

# Python
COPY ./ /UiTest
RUN pip config set global.index-url https://mirrors.aliyun.com/pypi/simple \
        && pip config set install.trusted-host mirrors.aliyun.com
RUN pip install pip -U
RUN pip install -r /UiTest/requirements.txt

ENTRYPOINT ["java","-jar","/UiTest/selenium-server-4.0.0-beta-4.jar","standalone"]
WORKDIR /UiTest
EXPOSE 4444