# TelemetryTrends (TTE) - Demo

**TelemetryTrends** é uma demo em Python / FastAPI que simula dispositivos IoT, ingere telemetria e serve como projeto para demonstrar CI/CD com **Azure DevOps** e automação via **PowerShell**.

## Tech stack
- Python 3.11, FastAPI, Pydantic
- Docker
- Azure DevOps (pipeline)
- PowerShell para deploy (usa `az` CLI)
- Opcional: InfluxDB + Grafana via Docker Compose

## Funcionalidades
- Endpoint `/telemetry` para ingestão de telemetria (POST).
- Endpoint `/metrics/{device_id}` para consulta dos últimos eventos (demo).
- Simulador de dispositivos que gera leituras periódicas (modo demo).
- Testes com `pytest`, lint com `flake8`.
- Dockerfile para containerização.
- Pipeline de CI/CD (azure-pipelines.yml): lint, tests, build e push para ACR + etapa que chama `deploy.ps1`.

## Como rodar local (venv)
```bash
python -m venv .venv
source .venv/bin/activate   # linux / mac
.venv\Scripts\Activate.ps1  # windows powershell
pip install -r src/requirements.txt
uvicorn telemetrytrends.main:app --reload --port 8000 --host 0.0.0.0

docker build -t telemetrytrends:local -f Dockerfile .
docker run --rm -p 8000:80 telemetrytrends:local
# acessar: http://localhost:8000/docs

docker-compose up --build
# FastAPI: http://localhost:8000/docs
# Grafana: http://localhost:3000 (admin:admin)

pip install -r src/requirements.txt
pytest -q

