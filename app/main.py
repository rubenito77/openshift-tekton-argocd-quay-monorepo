import os
import platform
import socket
from datetime import datetime, timezone

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

APP_NAME = os.getenv("APP_NAME", "app-demo")
APP_VERSION = os.getenv("APP_VERSION", "0.1.0")
ENVIRONMENT = os.getenv("ENVIRONMENT", "local")
IMAGE_TAG = os.getenv("IMAGE_TAG", "development")

app = FastAPI(
    title="OpenShift CI/CD Monorepo Demo",
    description="Aplicación para el laboratorio Tekton, Quay y Argo CD",
    version=APP_VERSION,
)


def runtime_information() -> dict:
    return {
        "application": APP_NAME,
        "version": APP_VERSION,
        "environment": ENVIRONMENT,
        "image_tag": IMAGE_TAG,
        "hostname": socket.gethostname(),
        "python": platform.python_version(),
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


@app.get("/", response_class=HTMLResponse)
def home() -> str:
    info = runtime_information()
    return f"""
    <!doctype html>
    <html lang="es">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>{info["application"]}</title>
      </head>
      <body>
        <main>
          <h1>{info["application"]}</h1>
          <p>Aplicación disponible</p>
          <dl>
            <dt>Versión</dt><dd>{info["version"]}</dd>
            <dt>Ambiente</dt><dd>{info["environment"]}</dd>
            <dt>Imagen</dt><dd>{info["image_tag"]}</dd>
            <dt>Pod</dt><dd>{info["hostname"]}</dd>
          </dl>
          <p><a href="/info">Información JSON</a> | <a href="/health">Health</a> | <a href="/docs">OpenAPI</a></p>
        </main>
      </body>
    </html>
    """


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "application": APP_NAME, "version": APP_VERSION}


@app.get("/ready")
def ready() -> dict:
    return {"status": "ready", "application": APP_NAME}


@app.get("/info")
def info() -> dict:
    return runtime_information()
