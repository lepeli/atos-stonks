FROM python:3.11-alpine

LABEL maintenair="Yvan <flash>"

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "index.py"]

EXPOSE 5000