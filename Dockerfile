FROM python:3.7  AS build-1

COPY ./ /UiTest
RUN pip install -U selenium
RUN pip install -U pytest
RUN pip install -U pytest-html
RUN pip install -U allure-pytest
RUN pip install -U PyYAML

FROM java:8 AS build-2
ADD selenium-server-4.0.0-beta-4.jar selenium-server-4.0.0-beta-4.jar
EXPOSE 4444
COPY --from=build-1 ./ /UiTest
RUN git config --global user.name "admin" \
    && git config --global user.email "admin@ezone.work" \
    && git config --global http.sslVerify false

ENTRYPOINT ["java","-jar","/selenium-server-4.0.0-beta-4.jar","standalone"]


FROM selenium/standalone-chrome:latest

COPY --from=build-2 ./ /UiTest


CMD ["python", "./run_case.py"]
