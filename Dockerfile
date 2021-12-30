FROM hub.kce.ksyun.com/ezone-public/python:3.9.6-alpine


COPY ./ /UiTest

RUN ["pip", "install", "--no-cache-dir",  "-r",  "./requirements.txt"]



CMD ["python", "./run_case.py"]
