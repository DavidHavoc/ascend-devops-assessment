"""Generate synthetic (fictional) seed data for the scheduling API.

All records produced here are fake and randomly generated. They are not real
people and contain no real personal or clinical information. Run:

    python scripts/generate_data.py

It overwrites data/clients.json, data/therapists.json, data/appointments.json.
A fixed random seed makes the output reproducible.
"""
import json
import random
from datetime import datetime, timedelta
from pathlib import Path

SEED = 42
DATA_DIR = Path(__file__).resolve().parent.parent / "data"
TODAY = datetime(2026, 10, 22)

FIRST = [
    "James", "Mary", "Robert", "Patricia", "John", "Jennifer", "Michael",
    "Linda", "David", "Elizabeth", "William", "Barbara", "Richard", "Susan",
    "Joseph", "Jessica", "Thomas", "Sarah", "Charles", "Karen", "Daniel",
    "Nancy", "Matthew", "Lisa", "Anthony", "Betty", "Mark", "Margaret",
    "Donald", "Sandra", "Steven", "Ashley", "Andrew", "Kimberly", "Joshua",
    "Emily", "Kenneth", "Donna", "Kevin", "Michelle", "Brian", "Carol",
    "George", "Amanda", "Edward", "Dorothy", "Ronald", "Melissa", "Timothy",
    "Deborah", "Jason", "Stephanie", "Jeffrey", "Rebecca", "Ryan", "Sharon",
    "Jacob", "Laura", "Gary", "Cynthia", "Nicholas", "Amy", "Eric", "Angela",
    "Jonathan", "Shirley", "Stephen", "Anna", "Larry", "Brenda",
]
LAST = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller",
    "Davis", "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez",
    "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin",
    "Lee", "Perez", "Thompson", "White", "Harris", "Sanchez", "Clark",
    "Ramirez", "Lewis", "Robinson", "Walker", "Young", "Allen", "King",
    "Wright", "Scott", "Torres", "Nguyen", "Hill", "Flores", "Green",
    "Adams", "Nelson", "Baker", "Hall", "Rivera", "Campbell", "Mitchell",
    "Carter", "Roberts", "Gomez", "Phillips", "Evans", "Turner", "Diaz",
    "Parker", "Cruz", "Edwards", "Collins", "Reyes", "Stewart", "Morris",
    "Morales", "Murphy", "Cook", "Rogers", "Gutierrez", "Ortiz", "Morgan",
]
EMAIL_DOMAINS = ["gmail.com", "yahoo.com", "outlook.com", "icloud.com",
                 "hotmail.com", "aol.com"]
CREDENTIALS = ["LCSW", "LCMHC", "LMFT", "PhD", "PsyD", "LCAS"]
SPECIALTIES = ["individual", "couples", "family", "child", "adolescent",
               "group", "assessment"]
APPT_TYPES = ["individual", "couples", "family", "assessment", "intake"]
MODALITIES = ["telehealth", "in_person"]


def _phone(rng):
    return f"+1 336 {rng.randint(200, 999)} {rng.randint(1000, 9999)}"


def _dob(rng):
    start = datetime(1950, 1, 1)
    end = datetime(2006, 12, 31)
    d = start + timedelta(days=rng.randint(0, (end - start).days))
    return d.strftime("%Y-%m-%d")


def _ts(dt):
    return dt.strftime("%Y-%m-%dT%H:%M:%S")


def generate():
    rng = random.Random(SEED)

    therapists = []
    for i in range(1, 19):
        fn, ln = rng.choice(FIRST), rng.choice(LAST)
        therapists.append({
            "id": i,
            "first_name": fn,
            "last_name": ln,
            "name": f"Dr. {fn} {ln}",
            "credentials": rng.choice(CREDENTIALS),
            "email": f"{fn.lower()}.{ln.lower()}@ascendpsy.com",
            "specialties": rng.sample(SPECIALTIES, rng.randint(1, 3)),
            "active": rng.random() > 0.08,
        })

    clients = []
    for n in range(450):
        cid = 1001 + n
        fn, ln = rng.choice(FIRST), rng.choice(LAST)
        created = datetime(2024, 1, 1) + timedelta(days=rng.randint(0, 640))
        clients.append({
            "id": cid,
            "first_name": fn,
            "last_name": ln,
            "name": f"{fn} {ln}",
            "email": f"{fn.lower()}.{ln.lower()}{rng.randint(1, 99)}@"
                     f"{rng.choice(EMAIL_DOMAINS)}",
            "phone": _phone(rng),
            "date_of_birth": _dob(rng),
            "status": "active" if rng.random() > 0.15 else "inactive",
            "created_at": _ts(created.replace(
                hour=rng.randint(8, 18), minute=rng.choice([0, 15, 30, 45]))),
        })

    appointments = []
    appt_id = 50001
    day0 = datetime(2026, 1, 5)
    for _ in range(6000):
        client = rng.choice(clients)
        therapist = rng.choice(therapists)
        day = day0 + timedelta(days=rng.randint(0, 180))
        while day.weekday() >= 5:
            day += timedelta(days=1)
        hour = rng.randint(9, 16)
        start = day.replace(hour=hour, minute=0, second=0)
        end = start + timedelta(minutes=50)
        if start < TODAY:
            status = rng.choices(
                ["completed", "cancelled", "no_show"], [0.70, 0.20, 0.10])[0]
        else:
            status = rng.choices(["scheduled", "cancelled"], [0.82, 0.18])[0]
        created = start - timedelta(days=rng.randint(3, 45))
        appointments.append({
            "id": appt_id,
            "client_id": client["id"],
            "therapist_id": therapist["id"],
            "start_time": _ts(start),
            "end_time": _ts(end),
            "status": status,
            "type": rng.choice(APPT_TYPES),
            "modality": rng.choice(MODALITIES),
            "created_at": _ts(created),
        })
        appt_id += 1

    appointments.sort(key=lambda a: a["start_time"])

    DATA_DIR.mkdir(exist_ok=True)
    for name, rows in [("therapists", therapists), ("clients", clients),
                       ("appointments", appointments)]:
        with open(DATA_DIR / f"{name}.json", "w", encoding="utf-8") as fh:
            json.dump(rows, fh, indent=2)
            fh.write("\n")
        print(f"{name}.json: {len(rows)} records")


if __name__ == "__main__":
    generate()
