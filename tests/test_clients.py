from app.storage import store


def test_list_clients(client):
    r = client.get("/clients")
    assert r.status_code == 200
    assert len(r.json()) == len(store.clients)


def test_get_client(client):
    client_id = next(iter(store.clients))
    r = client.get(f"/clients/{client_id}")
    assert r.status_code == 200
    assert r.json()["id"] == client_id


def test_get_missing_client(client):
    missing = max(store.clients) + 1000
    assert client.get(f"/clients/{missing}").status_code == 404


def test_client_appointments(client):
    client_id = store.appointments[0]["client_id"]
    r = client.get(f"/clients/{client_id}/appointments")
    assert r.status_code == 200
    body = r.json()
    assert len(body) >= 1
    assert all("client_name" in a for a in body)
