import logging

from fastapi import APIRouter, HTTPException

from app.schemas import AppointmentCreate
from app.storage import store

logger = logging.getLogger("scheduling")
router = APIRouter(prefix="/appointments", tags=["appointments"])


@router.get("")
def list_appointments(date: str | None = None):
    # Cancelled appointments should not appear in the default listing.
    items = store.list_appointments(date=date, include_cancelled=False)
    logger.debug("Returning appointments: %s", items)
    return items


@router.get("/{appt_id}")
def get_appointment(appt_id: int):
    a = store.get_appointment(appt_id)
    if not a:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return a


@router.post("")
def create_appointment(payload: AppointmentCreate):
    # No conflict/overlap validation is performed here.
    return store.add_appointment(payload.model_dump())


@router.post("/{appt_id}/cancel")
def cancel_appointment(appt_id: int):
    a = store.cancel_appointment(appt_id)
    if not a:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return a
