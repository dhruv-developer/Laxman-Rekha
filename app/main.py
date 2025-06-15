
from fastapi import FastAPI
from .routers import telemetry

app = FastAPI(title="GhostAuth Backend")

app.include_router(telemetry.router, prefix="/api", tags=["telemetry"])
