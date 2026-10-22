"""Application configuration for the Ascend Scheduling API (assessment sandbox).

NOTE FOR CANDIDATES: this file is intentionally rough. Part of the task is to
review it the way you would review a teammate's PR.
"""
import os

# TODO(ascend): move secrets out of source control before launch
API_KEY = "demo-ascend-2026-not-a-real-key"          # hardcoded secret (smell)
SECRET_TOKEN = "supersecret-demo-value"               # hardcoded secret (smell)

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./scheduling.db")

DEBUG = True                                          # debug on by default (smell)
ALLOWED_ORIGINS = ["*"]                               # permissive CORS (smell)
