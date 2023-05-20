from typing import Any, Optional

from aiofiles.os import path, remove
from fastapi import HTTPException
from sqlalchemy import delete
from sqlalchemy.future import select
from starlette import status

from apps.media.models import Media
from apps.tweet.models import Tweet, TweetLikes, TweetMediaReferences
from core.settings import settings


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
    own_uid: int,
    tweet_id: int,
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
    own_uid: int,
    tweet_id: int,
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


async def _delete_tweet_and_all_ref(session, tweet_id: int, own_uid: int) -> bool:
    async with session.begin():
        tweet_exists = await session.execute(
            select(Tweet.id).where(Tweet.id == tweet_id, Tweet.author == own_uid)
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
        medias_data = await session.execute(
            select(Media.media_path, Media.media_id)
            .join(TweetMediaReferences, TweetMediaReferences.media_id == Media.media_id)
            .where(TweetMediaReferences.tweet_id == tweet_id)
        )
    medias_data = medias_data.all()
    if medias_data:
        abs_media_path = [f"{settings.BASE_DIR}" + i[0] for i in medias_data]
        for i_path in abs_media_path:
            if await path.exists(path=i_path):
                await remove(path=i_path)
        async with session.begin():
            for i_media in medias_data:
                _ = await session.execute(
                    delete(Media).where(Media.media_id == i_media[1])
                )
            _ = await session.execute(
                delete(TweetMediaReferences).where(TweetMediaReferences == tweet_id)
            )
    async with session.begin():
        _ = await session.execute(
            delete(TweetLikes).where(TweetLikes.tweet_id == tweet_id)
        )
        res = await session.execute(delete(Tweet).where(Tweet.id == tweet_id))
    return True if res.rowcount >= 1 else False


async def _get_all_tweets(session) -> list[dict[Any]]:
    pass
