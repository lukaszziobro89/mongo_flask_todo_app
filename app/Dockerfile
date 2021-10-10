FROM python:3.7.5-alpine

RUN mkdir /app

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

#CMD flask run --host=0.0.0.0 --port=5000
CMD ["python", "main.py"]