# Changelog

All notable changes to this project are documented here.

## [0.1.0] - 2026-10-05

Initial prototype.

### Added
- FastAPI service with health, appointments, clients and therapists endpoints.
- In-memory data store backed by synthetic JSON seed data.
- Therapist availability and booking-conflict helpers.
- Seed data generator (`scripts/generate_data.py`).
- Starter `Dockerfile` and `docker-compose.yml`.
- Test suite and ruff configuration.
