# Mission2040 Intelligence Worker - Clean Dockerfile
FROM python:3.10-slim

# Debug: confirm python exists
RUN python3 --version

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy worker code
COPY . .

# Force correct working directory at runtime
WORKDIR /app

# Start intelligence worker
CMD ["python3", "mission2040_intelligence_worker.py"]
