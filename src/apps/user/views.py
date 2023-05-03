from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.future import select
from sqlalchemy.orm import aliased

from apps.user.models import FollowersReferences, User
from core.db.database import get_db

v1 = APIRouter()


@v1.get(path="/me")
async def get_me(api_key: str, session=Depends(get_db)) -> JSONResponse:
    async with session.begin():
        user = await session.execute(select(User).where(User.api_key == api_key))
    user = user.scalars().one_or_none()
    if user:
        user_1 = aliased(User, name="User1")
        user_2 = aliased(User, name="User2")
        async with session.begin():
            following = await session.execute(
                select(user_2.id, user_2.name)
                .select_from(user_1)
                .join(FollowersReferences, FollowersReferences.user_id == user_1.id)
                .join(user_2, user_2.id == FollowersReferences.follow)
                .where(user_1.id == user.id)
            )
        async with session.begin():
            follower = await session.execute(
                select(user_2.id, user_2.name)
                .select_from(user_1)
                .join(FollowersReferences, FollowersReferences.follow == user_1.id)
                .join(user_2, user_2.id == FollowersReferences.user_id)
                .where(user_1.id == user.id)
            )
        following = following.all()
        follower = follower.all()
        response_following = (
            [{"id": i[0], "name": i[1]} for i in following] if following else []
        )
        response_follower = (
            [{"id": i[0], "name": i[1]} for i in follower] if follower else []
        )
        response = {
            "result": "true",
            "user": {
                "id": user.id,
                "name": user.name,
                "followers": response_follower,
                "following": response_following,
            },
        }
    else:
        response = {
            "result": "false",
            "error_type": None,
            "error_message": "User not found",
        }

    return JSONResponse(status_code=200, content=response)
