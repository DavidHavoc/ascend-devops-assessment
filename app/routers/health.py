from fastapi import APIRouter

from app import __version__

router = APIRouter(tags=["health"])


@router.get("/")
def root():
    return {
        "service": "Ascend Scheduling API",
        "version": __version__,
        "docs": "/docs",
    }


@router.get("/health")
def health():
    return {"status": "ok"}


@router.get("/version")
def version():
    return {"version": __version__}
