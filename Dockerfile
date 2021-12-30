FROM hub.kce.ksyun.com/ezone-public/python:3.9.6-alpine


RUN git config --global user.name "admin" \
    && git config --global user.email "admin@ezone.work" \
    && git config --global http.sslVerify false

COPY ./ /UiTest

RUN yum -y install gcc
RUN pip install -i https://pypi.mirrors.ustc.edu.cn/simple/ -U selenium 
RUN pip install -U pytest
RUN pip install -U pytest-html
RUN pip install -U allure-pytest
RUN pip install -U PyYAML

RUN pip install -U zmail



CMD ["python", "./run_case.py"]
