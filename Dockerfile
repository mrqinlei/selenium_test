FROM hub.kce.ksyun.com/ezone-public/python:3.9.6-alpine


RUN git config --global user.name "admin" \
    && git config --global user.email "admin@ezone.work" \
    && git config --global http.sslVerify false

COPY ./ /UiTest

RUN ["pip", "install", "--no-cache-dir",  "-r",  "./requirements.txt"]



CMD ["python", "./run_case.py"]
