FROM selenium/standalone-chrome:latest

COPY ./ /UiTest



CMD ["python", "./run_case.py"]
