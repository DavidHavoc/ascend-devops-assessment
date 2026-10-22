# Ascend Scheduling API

![python](https://img.shields.io/badge/python-3.11%2B-blue)
![framework](https://img.shields.io/badge/FastAPI-0.115-009688)
![license](https://img.shields.io/badge/license-proprietary-lightgrey)
![status](https://img.shields.io/badge/status-prototype-orange)

Internal service that powers appointment scheduling across Ascend Psychological
Services: clients, therapists, availability and bookings. This is an early
prototype extracted into a standalone repository.

> **Note:** all data in `data/` is **synthetic** (randomly generated). There is
> no real client information in this repository.

## Table of contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Project structure](#project-structure)
- [Getting started](#getting-started)
- [API](#api)
- [Testing and quality](#testing-and-quality)
- [Configuration](#configuration)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## Overview

The Scheduling API exposes appointment data for internal tools: listing and
booking appointments, looking up clients, and checking therapist availability.
It is a FastAPI application with an in-memory data layer backed by JSON seed
files. It is deliberately early stage: the application logic works, but the
operational setup (containerization, CI, configuration handling) is still rough.

## Architecture

```
            +-------------------+
 client --> |     routers/      |   HTTP layer (FastAPI)
            +---------+---------+
                      |
            +---------v---------+
            |    services/      |   scheduling logic (availability, conflicts)
            +---------+---------+
                      |
            +---------v---------+
            |    storage.py     |   in-memory store, loads data/
            +---------+---------+
                      |
                 data/*.json        synthetic seed data
```

More detail in [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

## Project structure

```
app/
  main.py            app factory, middleware, router wiring
  storage.py         in-memory data store (loads data/)
  routers/           health, appointments, clients, therapists
  services/          scheduling logic
  ...                config, schemas, logging
data/                synthetic clients, therapists, appointments
scripts/             seed data generator
tests/               pytest suite
docs/                architecture and API reference
```

## Getting started

Requires Python 3.11+.

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
make install                   # or: pip install -r requirements.txt -r requirements-dev.txt
make run                       # uvicorn app.main:app --reload
```

Interactive docs: http://localhost:8000/docs

## API

Full reference in [docs/API.md](docs/API.md). Summary:

| Method | Path | Purpose |
| --- | --- | --- |
| GET | `/health` | Liveness check |
| GET | `/appointments` | List appointments (optional `date`) |
| POST | `/appointments` | Create an appointment |
| POST | `/appointments/{id}/cancel` | Cancel an appointment |
| GET | `/clients` | List clients |
| GET | `/clients/{id}/appointments` | A client's appointments |
| GET | `/therapists/{id}/availability` | A therapist's busy slots for a date |

## Testing and quality

```bash
make test      # pytest
make lint      # ruff check .
```

## Configuration

Configuration is read from environment variables; see
[.env.example](.env.example) for the supported keys.

## Deployment

A starter `Dockerfile` and `docker-compose.yml` are included but are not yet
production ready. Hardening the container and build pipeline is work in
progress.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

Proprietary. Internal use only. See [LICENSE](LICENSE).
