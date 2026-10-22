from datetime import datetime

from app.services.scheduling import overlaps, therapist_availability
from app.storage import store


def _t(s: str) -> datetime:
    return datetime.fromisoformat(s)


def test_overlaps_true():
    assert overlaps(_t("2026-02-02T09:00:00"), _t("2026-02-02T10:00:00"),
                    _t("2026-02-02T09:30:00"), _t("2026-02-02T10:30:00"))


def test_overlaps_adjacent_is_false():
    assert not overlaps(_t("2026-02-02T09:00:00"), _t("2026-02-02T10:00:00"),
                        _t("2026-02-02T10:00:00"), _t("2026-02-02T11:00:00"))


def test_availability_excludes_cancelled():
    target = next(a for a in store.appointments
                  if a["status"] == "cancelled")
    tid, day = target["therapist_id"], target["start_time"][:10]
    busy_starts = {b["start"] for b in therapist_availability(tid, day)}
    non_cancelled = {a["start_time"] for a in store.appointments
                     if a["therapist_id"] == tid
                     and a["start_time"][:10] == day
                     and a["status"] != "cancelled"}
    assert busy_starts == non_cancelled
