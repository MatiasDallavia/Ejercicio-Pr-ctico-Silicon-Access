FROM python:3.11.4-slim-buster

# set work directory
WORKDIR /usr/src/api

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y netcat

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/api/entrypoint.sh
RUN chmod +x /usr/src/api/entrypoint.sh


# copy project
COPY . .

EXPOSE 8000

# run entrypoint.sh
ENTRYPOINT ["/usr/src/api/entrypoint.sh"]

