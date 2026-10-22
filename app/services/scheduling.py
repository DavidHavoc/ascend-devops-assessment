"""Scheduling helpers: therapist availability and conflict detection."""
from datetime import datetime

from app.storage import store


def _parse(ts: str) -> datetime:
    return datetime.fromisoformat(ts)


def overlaps(a_start: datetime, a_end: datetime,
             b_start: datetime, b_end: datetime) -> bool:
    return a_start < b_end and b_start < a_end


def therapist_availability(therapist_id: int, date: str):
    """Return the busy slots for a therapist on a given date."""
    busy = []
    for a in store.appointments:
        if (a["therapist_id"] == therapist_id
                and a["start_time"].startswith(date)
                and a["status"] != "cancelled"):
            busy.append({"start": a["start_time"], "end": a["end_time"]})
    return busy


def has_conflict(therapist_id: int, start_time: str, end_time: str) -> bool:
    s, e = _parse(start_time), _parse(end_time)
    for a in store.appointments:
        if a["therapist_id"] != therapist_id or a["status"] == "cancelled":
            continue
        if overlaps(s, e, _parse(a["start_time"]), _parse(a["end_time"])):
            return True
    return False
