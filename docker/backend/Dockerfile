FROM python:3.9-slim-buster

WORKDIR /app

RUN pip install --upgrade pip
COPY requirements.txt requirements.txt

RUN pip install psycopg2_binary
RUN pip install --no-cache-dir -r requirements.txt

COPY ../../ .

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000","--reload"]