FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

# DO NOT expose any port
# DO NOT run uvicorn
# Render will treat this as a worker automatically

CMD ["python", "mission2040_intelligence_worker.py"]
