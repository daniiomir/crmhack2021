FROM python:3.7

RUN apt -y update
COPY . /app
WORKDIR /app
RUN pip install --upgrade pip
RUN apt install -y python3-dev python-multipart
RUN pip install -r requirements.txt

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "55555", "--reload"]