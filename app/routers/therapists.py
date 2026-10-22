from fastapi import APIRouter, HTTPException

from app.services.scheduling import therapist_availability
from app.storage import store

router = APIRouter(prefix="/therapists", tags=["therapists"])


@router.get("")
def list_therapists():
    return list(store.therapists.values())


@router.get("/{therapist_id}/availability")
def availability(therapist_id: int, date: str):
    if therapist_id not in store.therapists:
        raise HTTPException(status_code=404, detail="Therapist not found")
    return {
        "therapist_id": therapist_id,
        "date": date,
        "busy": therapist_availability(therapist_id, date),
    }
