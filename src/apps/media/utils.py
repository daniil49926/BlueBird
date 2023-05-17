from uuid import uuid4

import aiofiles
from fastapi import BackgroundTasks, File, HTTPException, status

from apps.media.models import Media
from core.settings import settings


async def check_and_load_media(
    session, background_task: BackgroundTasks, user_id: int, tweet_id: int, file: File
) -> int:
    file_path_to_bd = (
        f"/media/{user_id}_{tweet_id}_{uuid4()}.{file.filename.split('.')[-1]}"
    )
    file_abs_path = f"{settings.BASE_DIR}" + file_path_to_bd

    if file.content_type == "image/png":
        background_task.add_task(write_image, file_name=file_abs_path, file=file)
    else:
        raise HTTPException(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            detail={
                "result": "false",
                "error_type": None,
                "error_message": "It isn't png",
            },
        )
    new_media = Media(
        media_path=file_path_to_bd,
        media_name=file.filename,
        owner_id=user_id,
    )
    async with session.begin():
        session.add(new_media)

    return new_media.media_id


async def write_image(file_name: str, file: File) -> None:
    async with aiofiles.open(file_name, "wb") as buff:
        data = await file.read()
        await buff.write(data)
