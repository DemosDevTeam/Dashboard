FROM python:3.7.2

USER root

WORKDIR /app

ADD . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 8050

ENV NAME Dashboard

CMD ["python", "dashboard.py"]

