FROM python:3.11-slim

WORKDIR /app

COPY src/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r /app/requirements.txt

COPY src/ /app/src
ENV PYTHONPATH=/app/src
ENV TTE_START_SIMULATOR=false
EXPOSE 80
CMD ["uvicorn", "telemetrytrends.main:app", "--host", "0.0.0.0", "--port", "80"]
