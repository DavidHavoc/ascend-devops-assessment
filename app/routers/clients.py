from fastapi import APIRouter, HTTPException

from app.storage import store

router = APIRouter(prefix="/clients", tags=["clients"])


@router.get("")
def list_clients():
    return list(store.clients.values())


@router.get("/{client_id}")
def get_client(client_id: int):
    c = store.clients.get(client_id)
    if not c:
        raise HTTPException(status_code=404, detail="Client not found")
    return c


@router.get("/{client_id}/appointments")
def client_appointments(client_id: int):
    result = []
    for a in store.client_appointments(client_id):
        c = store.clients.get(client_id)
        result.append({**a, "client_name": c["name"] if c else None})
    return result
