from typing import Any

from fastapi import APIRouter, BackgroundTasks, Depends, File, UploadFile, status
from fastapi.responses import FileResponse, JSONResponse

from apps.auth.utils import get_current_active_user
from apps.media.utils import check_and_load_media, take_media
from apps.user.models import User
from core.db.database import get_db

v1 = APIRouter()


@v1.post("/")
async def load_medias(
    background_task: BackgroundTasks,
    current_user: User = Depends(get_current_active_user),
    file: UploadFile = File(...),
    session=Depends(get_db),
) -> JSONResponse:
    media_id = await check_and_load_media(
        session=session,
        background_task=background_task,
        user_id=current_user.id,
        file=file,
    )

    return JSONResponse(
        content={"result": True, "media_id": media_id},
        status_code=status.HTTP_201_CREATED,
    )


@v1.get("/")
async def take_medias_on_path(
    file_path: str,
    _: User = Depends(get_current_active_user),
) -> Any:
    real_file_path = await take_media(file_path)
    if real_file_path:
        return FileResponse(real_file_path)
    return JSONResponse(
        content={"result": False}, status_code=status.HTTP_404_NOT_FOUND
    )
