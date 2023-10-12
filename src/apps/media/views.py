from fastapi import APIRouter, BackgroundTasks, Depends, File, UploadFile, status
from fastapi.responses import JSONResponse

from apps.auth.utils import get_current_active_user
from apps.media.utils import check_and_load_media
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
