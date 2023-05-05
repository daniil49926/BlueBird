from sqlalchemy.future import select
from sqlalchemy.orm import aliased

from apps.user.models import FollowersReferences, User


async def get_user_by_key(session, api_key: str) -> User:
    async with session.begin():
        user = await session.execute(select(User).where(User.api_key == api_key))
    return user.scalars().one_or_none()


async def get_user_by_id(session, id_: int) -> User:
    async with session.begin():
        user = await session.execute(select(User).where(User.id == id_))
    return user.scalars().one_or_none()


async def get_follower_and_following_by_user(session, user_in: User):
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
