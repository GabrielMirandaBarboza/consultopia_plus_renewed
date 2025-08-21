from fastapi import FastAPI, Request, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware

from prometheus_client import Counter, Histogram
import time

app = FastAPI(title="Consultopia V5", version=1.0)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"]
)

#metricas
REQUEST_COUNT = Counter("http_requests_total", "Total de Requisições", ["method", "endpoint"])
REQUEST_LATENCY = Histogram("http_request_duration", "Tempo de Resposta", ["endpoint"])

@app.middleware("http")
async def metrics_middleware(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time

    endpoint = request.url.path
    REQUEST_COUNT.labels(request.method,endpoint).inc()
    REQUEST_LATENCY.labels(endpoint).observe(process_time)
    return response

ACCESS_CODE = "899a3e86-dcd5-4c2d-9ce3-467dc3e55383"

def verificar_codigo(request: Request):
    codigo = request.headers.get("Authorization")
    if codigo != f"Bearer {ACCESS_CODE}":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Código de acesso inválido",
            headers={"WWW-Authenticate": "Bearer"}
        )