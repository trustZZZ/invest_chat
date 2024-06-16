FROM python:3.11

RUN mkdir /chat

WORKDIR /chat

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod a+x /chat/docker/*.sh

CMD ["gunicorn", "app.main:app", "--workers", "1", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind=0.0.0.0:3000"]
