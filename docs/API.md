# API reference

Base URL (local): `http://localhost:8000`

Interactive docs are served at `/docs` (Swagger UI) and `/redoc`.

## Health

### `GET /health`
Liveness check.
```json
{ "status": "ok" }
```

## Appointments

### `GET /appointments`
List appointments. Optional query parameter `date` (format `YYYY-MM-DD`).
```
GET /appointments?date=2026-03-04
```

### `GET /appointments/{id}`
Return a single appointment, or `404` if it does not exist.

### `POST /appointments`
Create an appointment.
```json
{
  "client_id": 1001,
  "therapist_id": 3,
  "start_time": "2026-03-04T10:00:00",
  "end_time": "2026-03-04T10:50:00",
  "type": "individual"
}
```

### `POST /appointments/{id}/cancel`
Cancel an appointment. Returns the updated record, or `404`.

## Clients

### `GET /clients`
List all clients.

### `GET /clients/{id}`
Return a single client, or `404`.

### `GET /clients/{id}/appointments`
List a client's appointments, each annotated with the client's name.

## Therapists

### `GET /therapists`
List all therapists.

### `GET /therapists/{id}/availability`
Return a therapist's busy slots for a date (required `date` query parameter).
```
GET /therapists/3/availability?date=2026-03-04
```
```json
{
  "therapist_id": 3,
  "date": "2026-03-04",
  "busy": [ { "start": "2026-03-04T10:00:00", "end": "2026-03-04T10:50:00" } ]
}
```
