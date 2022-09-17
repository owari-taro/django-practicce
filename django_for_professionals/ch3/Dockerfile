FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
#dont write pyc
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY Pipfile Pipfile.lock requirements.txt /code/
#できるだけ一行にまとめる.別々にするとlayerがRUNのたびに作られてしまう
RUN  pip install pipenv && pipenv sync --system

COPY . /code/