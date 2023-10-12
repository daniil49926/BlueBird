from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse

from apps.auth.utils import get_current_active_user
from apps.tweet.utils import (
    _create_tweet_and_ref,
    _delete_tweet_and_all_ref,
    _get_all_tweets,
    _get_tweet_by_uid,
    _like_tweet_with_uid,
    _unliked_tweet_with_uid,
)
from apps.user.models import User
from core.db.database import get_db

v1 = APIRouter()


@v1.post("/")
async def create_tweet(
    tweet_data: dict,
    current_user: User = Depends(get_current_active_user),
    session=Depends(get_db),
) -> JSONResponse:
    tweet_content = tweet_data.get("tweet_data")
    tweet_media_ids = tweet_data.get("tweet_media_ids")
    tweet_id = await _create_tweet_and_ref(
        session=session,
        own_uid=current_user.id,
        tweet_content=tweet_content,
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
    current_user: User = Depends(get_current_active_user),
    session=Depends(get_db),
) -> JSONResponse:
    ok = await _delete_tweet_and_all_ref(
        session=session, tweet_id=tid, own_uid=current_user.id
    )
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


@v1.get("/{uid}")
async def get_tweet_by_uid(
    uid: int,
    _: User = Depends(get_current_active_user),
    session=Depends(get_db),
) -> JSONResponse:
    tweet = await _get_tweet_by_uid(session=session, uid=uid)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"result": "true", "tweets": tweet},
    )


@v1.post("/{tid}/likes")
async def liked_tweet(
    tid: int,
    current_user: User = Depends(get_current_active_user),
    session=Depends(get_db),
) -> JSONResponse:
    await _like_tweet_with_uid(session=session, own_uid=current_user.id, tweet_id=tid)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "result": "true",
        },
    )


@v1.delete("/{tid}/likes")
async def unliked_tweet(
    tid: int,
    current_user: User = Depends(get_current_active_user),
    session=Depends(get_db),
) -> JSONResponse:
    ok = await _unliked_tweet_with_uid(
        session=session, own_uid=current_user.id, tweet_id=tid
    )
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
    _: User = Depends(get_current_active_user),
    session=Depends(get_db),
) -> JSONResponse:
    tweets = await _get_all_tweets(session=session)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"result": "true", "tweets": tweets},
    )
