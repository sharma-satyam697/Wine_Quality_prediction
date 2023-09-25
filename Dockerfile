FROM python:3.11.1-slim-buster

RUN apt update -y && install apt awscli -y
WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt

CMD ["python3", "app.p"]