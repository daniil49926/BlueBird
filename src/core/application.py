from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.service.routers import router as core_router


_app = None


def get_app():
    global _app
    if not _app:
        _app = FastAPI(title="BlueBird", version="0.1.1", description="")
        _app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["GET", "POST"],
            allow_headers=["*"],
        )
        _app.include_router(core_router)

    return _app
