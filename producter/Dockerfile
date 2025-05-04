FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r Requirements.txt

CMD ["python", "-u", "producer.py"]
