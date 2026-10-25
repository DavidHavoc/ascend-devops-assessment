"""Application configuration for the Ascend Scheduling API (assessment sandbox).

NOTE FOR CANDIDATES: this file is intentionally rough. Part of the task is to
review it the way you would review a teammate's PR.
"""
import os


def env_bool(name: str, default: bool = False) -> bool:
    return os.getenv(name, str(default)).strip().lower() in {
        "1", "true", "yes", "on",
    }


# TODO(ascend): move secrets out of source control before launch
API_KEY = "demo-ascend-2026-not-a-real-key"          # hardcoded secret (smell)
SECRET_TOKEN = "supersecret-demo-value"               # hardcoded secret (smell)

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./scheduling.db")

DEBUG = env_bool("DEBUG", default=False)
ALLOWED_ORIGINS = [
    origin.strip()
    for origin in os.getenv(
        "ALLOWED_ORIGINS",
        "http://localhost:3000,http://127.0.0.1:3000",
    ).split(",")
    if origin.strip()
]
