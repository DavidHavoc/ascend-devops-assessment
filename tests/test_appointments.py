"""One test here is expected to FAIL on a fresh checkout. It documents a bug
you are asked to find and fix (see ASSESSMENT.md, task 1). The rest pass.

Tests derive their expectations from the data so they survive regeneration."""
from collections import defaultdict

from app.storage import store


def _date_with_cancelled() -> str:
    """A date that has both a cancelled and a non-cancelled appointment."""
    by_date = defaultdict(set)
    for a in store.appointments:
        by_date[a["start_time"][:10]].add(a["status"])
    for day, statuses in sorted(by_date.items()):
        if "cancelled" in statuses and len(statuses) > 1:
            return day
    raise AssertionError("dataset has no suitable date")


def test_list_by_date(client):
    day = store.appointments[0]["start_time"][:10]
    r = client.get("/appointments", params={"date": day})
    assert r.status_code == 200
    assert {a["start_time"][:10] for a in r.json()} == {day}


def test_cancelled_excluded_by_default(client):
    day = _date_with_cancelled()
    r = client.get("/appointments", params={"date": day})
    assert "cancelled" not in {a["status"] for a in r.json()}


def test_get_single(client):
    appt_id = store.appointments[0]["id"]
    r = client.get(f"/appointments/{appt_id}")
    assert r.status_code == 200
    assert r.json()["id"] == appt_id


def test_get_missing_returns_404(client):
    missing = max(a["id"] for a in store.appointments) + 1000
    assert client.get(f"/appointments/{missing}").status_code == 404


def test_create(client):
    therapist_id = next(iter(store.therapists))
    client_id = next(iter(store.clients))
    payload = {
        "client_id": client_id, "therapist_id": therapist_id,
        "start_time": "2026-12-01T09:00:00",
        "end_time": "2026-12-01T09:50:00", "type": "individual",
    }
    r = client.post("/appointments", json=payload)
    assert r.status_code == 200
    assert r.json()["status"] == "scheduled"


def test_cancel(client):
    appt_id = store.appointments[0]["id"]
    r = client.post(f"/appointments/{appt_id}/cancel")
    assert r.status_code == 200
    assert r.json()["status"] == "cancelled"
