FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

# Do NOT expose port
# Do NOT use uvicorn
# This runs as a pure worker
CMD ["python", "mission2040_intelligence_worker.py"]
