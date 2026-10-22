# DevOps Engineer — Technical Assessment

Welcome, and thank you for your time. This is a small, self-contained task.
Everything in the repository is synthetic. There is no real client data of any
kind.

**Time:** Aim for **60 to 90 minutes**. A smaller, well reasoned and well
explained submission beats a rushed attempt at everything. If you run out of
time, stop and write up what you would do next.

---

## How we'd like you to work (please read)

- Open the repo in **Cursor as an IDE** (editor with inline and chat
  assistance). **Please do not use fully autonomous Agent mode** for this task.
  We want to see *you* drive: read the code, decide what to change, and apply
  changes yourself.
- Using AI assistance, Cursor's chat and inline suggestions, and web search is
  **encouraged**, but review every suggestion and stay in control of what
  lands. When you accept or reject a suggestion, say briefly *why*.
- **Record your screen** while you work and narrate your thinking as you go. A
  screen recording is enough; no webcam needed.

We are evaluating your **judgment and reasoning**, not whether you can type
everything from memory.

---

## The repository

This is a small FastAPI service that serves synthetic appointment data for a
scheduling tool. It builds and runs, but it is rough in several places, roughly
the state of an early internal prototype.

### Layout

```
app/
  main.py            app entry (routers wired here)
  storage.py         data access (loads data/)
  routers/           API endpoints
  services/          scheduling logic
  ...                config, schemas, logging
data/                synthetic clients, therapists, appointments
tests/               pytest suite
Dockerfile           starter, needs work
docker-compose.yml   starter, needs work
.github/workflows/   add your CI here
Makefile, pyproject.toml, requirements*.txt, NOTES.md
```

### Endpoints

```
GET  /health
GET  /appointments?date=YYYY-MM-DD
GET  /appointments/{id}
POST /appointments
POST /appointments/{id}/cancel
GET  /clients
GET  /clients/{id}
GET  /clients/{id}/appointments
GET  /therapists
GET  /therapists/{id}/availability?date=YYYY-MM-DD
```

### Run it

```
make install     # or: pip install -r requirements.txt -r requirements-dev.txt
make run         # uvicorn app.main:app --reload ; docs at localhost:8000/docs
make test        # pytest ; one test fails on a fresh checkout (task 1)
make lint        # ruff check .
```

---

## Your tasks

### Core (please attempt these)

1. **Find and fix the bug.** One test fails on a fresh checkout. Work out why,
   fix the underlying behaviour (not the test), and make the suite pass.
2. **Review the code and config for problems.** There are several questionable
   practices in this repo (correctness, security, and operational). Identify
   them and fix the ones you consider most important. Note anything you spot but
   choose not to fix, and why.
3. **Containerize it properly.** Improve the `Dockerfile` so it's suitable for a
   real deployment (think: image size, build caching, running as non-root,
   health, not shipping things that shouldn't ship).
4. **Add CI.** Add a GitHub Actions workflow that builds the image, runs the
   linter, and runs the tests on every push.

### Stretch (optional, only if time allows)

5. **Local orchestration.** Improve `docker-compose.yml` so the API and its
   dependency come up reliably for local development.
6. **One reliability or observability improvement** of your choice (a meaningful
   health check, structured logging, a basic metric, or a small Terraform
   snippet). Explain the choice.

---

## Deliverables

1. Your changed code: push to the repo, or send a patch or diff.
2. Your **screen recording**.
3. **`NOTES.md`** filled in: your approach, the problems you found, what you used
   your tools and AI for, trade-offs you made, and what you'd do next.

---

## What we're looking for

| We value                                   | We are **not** testing              |
|--------------------------------------------|-------------------------------------|
| How you break the problem down             | Memorizing syntax                   |
| Spotting the security and correctness issues | A flawless, complete product      |
| Effective **and critical** use of AI tools | Working without any help            |
| Clear reasoning for each decision          | Doing it the way we would           |

---

## A note on privacy

Your recording and submission are used only to evaluate your application, viewed
only by the hiring team, and deleted after the process closes. If you'd prefer a
live session instead of a recording, just let us know. That is completely fine.
