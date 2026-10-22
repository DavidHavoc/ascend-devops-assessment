# Contributing

Internal guide for working in this repository.

## Setup

```bash
make install
make run
```

## Workflow

1. Branch from `main` using `feature/<short-description>` or
   `fix/<short-description>`.
2. Keep changes focused; write a clear PR description of what and why.
3. Make sure tests and lint pass before opening a PR:
   ```bash
   make test
   make lint
   ```
4. At least one review approval is required to merge.

## Conventions

- Python formatted and linted with **ruff** (`make lint`).
- Keep HTTP concerns in `routers/`, domain logic in `services/`, and data
  access in `storage.py`.
- Tests live in `tests/` and should not depend on each other.

## Commit messages

Short imperative subject line, e.g. `Add therapist availability endpoint`.
Reference an issue where relevant.
