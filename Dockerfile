FROM python:3.7


RUN git config --global user.name "admin" \
    && git config --global user.email "admin@ezone.work" \
    && git config --global http.sslVerify false

COPY ./ /UiTest


RUN pip install -U selenium 
RUN pip install -U pytest
RUN pip install -U pytest-html
RUN pip install -U allure-pytest
RUN pip install -U PyYAML

RUN pip install -U zmail



CMD ["python", "./run_case.py"]
