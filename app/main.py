"""Ascend Scheduling API — assessment sandbox.

A deliberately imperfect early-prototype service. See ASSESSMENT.md.
All data in this repo is synthetic; there is no real client information.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app import config
from app.logging_config import configure_logging
from app.routers import appointments, clients, health, therapists

configure_logging(config.DEBUG)


def create_app() -> FastAPI:
    app = FastAPI(title="Ascend Scheduling API (Assessment)", version="0.1.0")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=config.ALLOWED_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(health.router)
    app.include_router(appointments.router)
    app.include_router(clients.router)
    app.include_router(therapists.router)
    return app


app = create_app()
