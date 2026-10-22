from pydantic import BaseModel


class Client(BaseModel):
    id: int
    name: str
    email: str
    phone: str


class Therapist(BaseModel):
    id: int
    name: str
    specialties: list[str]


class Appointment(BaseModel):
    id: int
    client_id: int
    therapist_id: int
    start_time: str
    end_time: str
    status: str
    type: str


class AppointmentCreate(BaseModel):
    client_id: int
    therapist_id: int
    start_time: str
    end_time: str
    type: str
