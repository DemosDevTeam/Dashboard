FROM ubuntu:16.04

# MAINTANER Your Name "lexokan@gmail.com"

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app    

RUN pip install --upgrade pip \
    pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "dashboard.py" ]
# FROM python:3.6.7
# ADD . /code
# WORKDIR /code
# RUN pip install -r requirements.txt
# CMD python app.py
# FROM python:3.4-alpine
# ADD . /code
# WORKDIR /code
# RUN pip install -r requirements.txt
# CMD ["python", "dashboard.py"]