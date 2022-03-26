FROM selenium/standalone-chrome:96.0

COPY ./ /UiTest
RUN sudo apt-get update && sudo apt-get -y install python3-pip allure
RUN sudo pip install -r /UiTest/requirements.txt
RUN sudo chown -R seluser /UiTest
RUN sudo ln -s /UiTest/allure/bin/allure /usr/bin/allure

EXPOSE 4444
WORKDIR /UiTest
