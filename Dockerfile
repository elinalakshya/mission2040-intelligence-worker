# Mission2040 Intelligence Worker - Clean Dockerfile
FROM python:3.10-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy worker code
COPY . /app/

# Start the intelligence worker
CMD ["python", "mission2040_intelligence_worker.py"]
