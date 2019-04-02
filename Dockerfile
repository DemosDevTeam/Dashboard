FROM python:3.7.2

USER root

WORKDIR /app

ADD . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 8050

ENV NAME Dashboard

CMD ["python", "dashboard.py"]


# FROM ubuntu:16.04

# MAINTANER Your Name "lexokan@gmail.com"

# RUN apt-get update -y && \
#     apt-get install -y python-pip python-dev

# # We copy just the requirements.txt first to leverage Docker cache

<<<<<<< HEAD
# We copy just the requirements.txt first to leverage Docker cache
#COPY ./requirements.txt /app/requirements.txt

# WORKDIR /app    

RUN pip install --upgrade pip
RUN pip install -r ./requirements.txt 

#COPY . /app
=======
# COPY ./requirements.txt /app/requirements.txt

# WORKDIR /app    

# RUN pip install --upgrade pip \
#     pip install -r requirements.txt

# # COPY . /app
>>>>>>> dbd02a7bad72760d4aed345f654e1238fa095990

# ENTRYPOINT [ "python" ]

# CMD [ "python ", "dashboard.py" ]
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
