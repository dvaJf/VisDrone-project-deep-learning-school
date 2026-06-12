FROM python:3.11-slim
WORKDIR /app

RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    libxcb1 \
    libx11-6 \
    libxext6 \
    libsm6 \
    libxrender1 \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

ENV YOLO_CONFIG_DIR=/tmp/Ultralytics
RUN mkdir -p /tmp/Ultralytics && chmod 777 /tmp/Ultralytics

COPY requirements.txt .
RUN pip install --timeout 300 --no-cache-dir -r requirements.txt

COPY main.py .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]