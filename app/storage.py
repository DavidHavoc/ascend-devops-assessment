"""In-memory data store backed by the synthetic JSON files in data/."""
import json
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def _load(name: str):
    with open(DATA_DIR / name, "r", encoding="utf-8") as fh:
        return json.load(fh)


class Store:
    def __init__(self) -> None:
        self.clients = {c["id"]: c for c in _load("clients.json")}
        self.therapists = {t["id"]: t for t in _load("therapists.json")}
        self.appointments = _load("appointments.json")

    def reset(self) -> None:
        """Reload from disk — used to isolate tests."""
        self.__init__()

    def list_appointments(self, date: str | None = None,
                          include_cancelled: bool = False):
        items = self.appointments
        if date:
            items = [a for a in items if a["start_time"].startswith(date)]
        if not include_cancelled:
            items = [a for a in items if a["status"] != "cancelled"]
        return items

    def get_appointment(self, appt_id: int):
        return next((a for a in self.appointments if a["id"] == appt_id), None)

    def client_appointments(self, client_id: int):
        return [a for a in self.appointments if a["client_id"] == client_id]

    def add_appointment(self, data: dict):
        new_id = max((a["id"] for a in self.appointments), default=0) + 1
        record = {**data, "id": new_id, "status": "scheduled"}
        self.appointments.append(record)
        return record

    def cancel_appointment(self, appt_id: int):
        a = self.get_appointment(appt_id)
        if a:
            a["status"] = "cancelled"
        return a


store = Store()
