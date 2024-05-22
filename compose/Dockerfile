FROM python:3.10

RUN pip install --upgrade pip
RUN apt -y update

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . /app

COPY ./compose/start /start
RUN sed -i 's/\r//' /start
RUN chmod +x /start

WORKDIR /app