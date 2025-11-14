RUN python3 --version

FROM python:3.10-slim

RUN python3 --version

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

WORKDIR /app

CMD ["python", "mission2040_intelligence_worker.py"]
