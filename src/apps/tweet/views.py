from typing import Annotated, Optional

from fastapi import APIRouter, Depends, Header, HTTPException, status
from fastapi.responses import JSONResponse

from apps.tweet.utils import _create_tweet_and_ref
from apps.user.utils import get_user_by_key
from core.db.database import get_db

v1 = APIRouter()


@v1.post("/")
async def create_tweet(
    tweet_data: str,
    tweet_media_ids: Optional[list[int] | None],
    api_key: Annotated[str | None, Header()],
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
    tweet_id = await _create_tweet_and_ref(
        session=session,
        own_uid=user.id,
        tweet_content=tweet_data,
        tweet_media_ids=tweet_media_ids,
    )
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "result": "true",
            "tweet_id": tweet_id,
        },
    )
