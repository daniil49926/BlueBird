from typing import Optional

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
