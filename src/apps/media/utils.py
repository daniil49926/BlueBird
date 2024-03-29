import os
from typing import Any
from uuid import uuid4

import aiofiles
from aiofiles.os import makedirs, path
from fastapi import BackgroundTasks, File, HTTPException, status

from apps.media.models import Media
from core.settings import settings


async def check_and_load_media(
    session, background_task: BackgroundTasks, user_id: int, file: File
) -> int:
    file_path_to_bd = f"/media/{user_id}_{uuid4()}.{file.filename.split('.')[-1]}"
    p_path = os.path.dirname(settings.BASE_DIR)
    file_abs_path = f"{p_path}" + "/static" + file_path_to_bd

    if file.content_type == "image/png" or file.content_type == "image/jpeg":
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
    head = "/".join(file_name.split("/")[0:-1])
    if not await path.exists(head):
        await makedirs(head)
    async with aiofiles.open(file_name, "wb") as buff:
        data = await file.read()
        await buff.write(data)


async def take_media(media_path: str) -> Any:
    p_path = os.path.dirname(settings.BASE_DIR)
    media_path = f"{p_path}" + "/static" + media_path
    if await path.isfile(media_path):
        return media_path
    return None
