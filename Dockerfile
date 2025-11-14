FROM python:3.10-slim

# Prevent Render from treating this as a Web Service
EXPOSE 1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "mission2040_intelligence_worker.py"]
