from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from apps.user.utils import get_user_by_key, get_follower_and_following_by_user
from core.db.database import get_db

v1 = APIRouter()


@v1.get(path="/me")
async def get_me(api_key: str, session=Depends(get_db)) -> JSONResponse:
    user = await get_user_by_key(session=session, api_key=api_key)
    if user:
        response_following, response_follower = await get_follower_and_following_by_user(
            session=session,
            user_in=user
        )
        return JSONResponse(
            status_code=200,
            content={
                "result": "true",
                "user": {
                    "id": user.id,
                    "name": user.name,
                    "followers": response_follower,
                    "following": response_following,
                }
            }
        )
    else:
        return JSONResponse(
            status_code=404,
            content={
                "result": "false",
                "error_type": None,
                "error_message": "User not found",
            }
        )
