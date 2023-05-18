from typing import Annotated

from fastapi import (
    APIRouter,
    BackgroundTasks,
    Depends,
    File,
    Header,
    HTTPException,
    UploadFile,
    status,
)
from fastapi.responses import JSONResponse

from apps.media.utils import check_and_load_media
from apps.user.utils import get_user_by_key
from core.db.database import get_db

v1 = APIRouter()


@v1.post("/")
async def load_medias(
    background_task: BackgroundTasks,
    api_key: Annotated[str | None, Header()],
    file: UploadFile = File(...),
    session=Depends(get_db),
) -> JSONResponse:
    user = await get_user_by_key(session=session, api_key=api_key)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={
                "result": "false",
                "error_type": None,
                "error_message": "Not authenticated",
            },
        )
    media_id = await check_and_load_media(
        session=session,
        background_task=background_task,
        user_id=user.id,
        file=file,
    )

    return JSONResponse(
        content={"result": True, "media_id": media_id},
        status_code=status.HTTP_201_CREATED,
    )
