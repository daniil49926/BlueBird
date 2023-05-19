from typing import Optional

from fastapi import HTTPException
from sqlalchemy import delete
from sqlalchemy.future import select
from starlette import status

from apps.tweet.models import Tweet, TweetLikes, TweetMediaReferences


async def _create_tweet_and_ref(
    session,
    own_uid: int,
    tweet_content: str,
    tweet_media_ids: Optional[list[int] | None],
) -> int:
    new_t = Tweet(
        content=tweet_content,
        author=own_uid,
    )
    async with session.begin():
        session.add(new_t)
    if tweet_media_ids:
        ref_tweet_media_data = []
        for media_id in tweet_media_ids:
            ref_tweet_media_data.append(
                TweetMediaReferences(tweet_id=new_t.id, media_id=media_id)
            )
        async with session.begin():
            session.add_all(ref_tweet_media_data)
    return new_t.id


async def _like_tweet_with_uid(
    session,
    own_uid,
    tweet_id,
) -> None:
    async with session.begin():
        tweet_exists = await session.execute(
            select(Tweet.id).where(Tweet.id == tweet_id)
        )
    if not tweet_exists.scalars().one_or_none():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "result": "false",
                "error_type": None,
                "error_message": "Tweet not found",
            },
        )
    new_l = TweetLikes(tweet_id=tweet_id, user_id=own_uid)
    async with session.begin():
        session.add(new_l)


async def _unliked_tweet_with_uid(
    session,
    own_uid,
    tweet_id,
) -> bool:
    async with session.begin():
        tweet_exists = await session.execute(
            select(Tweet.id).where(Tweet.id == tweet_id)
        )
    if not tweet_exists.scalars().one_or_none():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "result": "false",
                "error_type": None,
                "error_message": "Tweet not found",
            },
        )
    async with session.begin():
        res = await session.execute(
            delete(TweetLikes).where(
                TweetLikes.user_id == own_uid,
                TweetLikes.tweet_id == tweet_id,
            )
        )
    return True if res.rowcount >= 1 else False
