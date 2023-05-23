from typing import Annotated, Optional

from fastapi import APIRouter, Depends, Header, HTTPException, status
from fastapi.responses import JSONResponse

from apps.tweet.utils import (
    _create_tweet_and_ref,
    _delete_tweet_and_all_ref,
    _get_all_tweets,
    _get_tweet,
    _like_tweet_with_uid,
    _unliked_tweet_with_uid,
)
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


@v1.delete("/{tid}")
async def delete_tweet(
    tid: int,
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
    ok = await _delete_tweet_and_all_ref(session=session, tweet_id=tid, own_uid=user.id)
    if not ok:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={
                "result": "false",
                "error_type": None,
                "error_message": "Server error",
            },
        )
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "result": "true",
        },
    )


@v1.get("/{tid}")
async def get_tweet(
    tid: int,
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
    tweet = await _get_tweet(session=session, tid=tid)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"result": "true", "tweets": tweet},
    )


@v1.post("/{tid}/likes")
async def liked_tweet(
    tid: int,
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
    await _like_tweet_with_uid(session=session, own_uid=user.id, tweet_id=tid)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "result": "true",
        },
    )


@v1.delete("/{tid}/likes")
async def unliked_tweet(
    tid: int,
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
    ok = await _unliked_tweet_with_uid(session=session, own_uid=user.id, tweet_id=tid)
    if not ok:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={
                "result": "false",
                "error_type": None,
                "error_message": "Server error",
            },
        )
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"result": "true"},
    )


@v1.get("/")
async def get_tweets(
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
    tweets = await _get_all_tweets(session=session)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"result": "true", "tweets": tweets},
    )
