from sqlalchemy.future import select
from sqlalchemy.orm import aliased
from sqlalchemy import delete

from apps.user.models import FollowersReferences, User


async def _get_user_by_key(session, api_key: str) -> User:
    async with session.begin():
        user = await session.execute(select(User).where(User.api_key == api_key))
    return user.scalars().one_or_none()


async def _get_user_by_id(session, id_: int) -> User:
    async with session.begin():
        user = await session.execute(select(User).where(User.id == id_))
    return user.scalars().one_or_none()


async def _get_follower_and_following_by_user(session, user_in: User):
    user_1 = aliased(User, name="User1")
    user_2 = aliased(User, name="User2")
    async with session.begin():
        following = await session.execute(
            select(user_2.id, user_2.name)
            .select_from(user_1)
            .join(FollowersReferences, FollowersReferences.user_id == user_1.id)
            .join(user_2, user_2.id == FollowersReferences.follow)
            .where(user_1.id == user_in.id)
        )
    async with session.begin():
        follower = await session.execute(
            select(user_2.id, user_2.name)
            .select_from(user_1)
            .join(FollowersReferences, FollowersReferences.follow == user_1.id)
            .join(user_2, user_2.id == FollowersReferences.user_id)
            .where(user_1.id == user_in.id)
        )
    following = following.all()
    follower = follower.all()
    return (
        [{"id": i[0], "name": i[1]} for i in following] if following else [],
        [{"id": i[0], "name": i[1]} for i in follower] if follower else [],
    )


async def checking_sub_capability(
    following_uid: int, follower_uid: int, session
) -> bool:
    if following_uid == follower_uid:
        return False
    async with session.begin():
        entry = await session.execute(
            select(FollowersReferences).where(
                FollowersReferences.user_id == following_uid,
                FollowersReferences.follow == follower_uid,
            )
        )
    return False if entry.scalars().one_or_none() else True


async def _follow_user(following_uid: int, follower_uid: int, session) -> bool:
    if not await checking_sub_capability(
        following_uid=following_uid, follower_uid=follower_uid, session=session
    ):
        return False
    new_entry = FollowersReferences(user_id=following_uid, follow=follower_uid)
    async with session.begin():
        session.add(new_entry)
    return True


async def _unfollow_user(following_uid: int, follower_uid: int, session) -> bool:
    async with session.begin():
        res = await session.execute(
            delete(FollowersReferences).where(
                FollowersReferences.user_id == following_uid,
                FollowersReferences.follow == follower_uid,
            )
        )
    return True if res.rowcount >= 1 else False
