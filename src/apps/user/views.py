from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse

from apps.user.utils import (
    _follow_user,
    _get_follower_and_following_by_user,
    _get_user_by_id,
    _get_user_by_key,
)
from core.db.database import get_db

v1 = APIRouter()


@v1.get(path="/me")
async def get_me(api_key: str, session=Depends(get_db)) -> JSONResponse:
    user = await _get_user_by_key(session=session, api_key=api_key)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={
                "result": "false",
                "error_type": None,
                "error_message": "Not authenticated",
            },
        )
    (
        response_following,
        response_follower,
    ) = await _get_follower_and_following_by_user(session=session, user_in=user)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "result": "true",
            "user": {
                "id": user.id,
                "name": user.name,
                "followers": response_follower,
                "following": response_following,
            },
        },
    )


@v1.get("/{uid}")
async def get_user(uid: int, api_key: str, session=Depends(get_db)) -> JSONResponse:
    if not await _get_user_by_key(session=session, api_key=api_key):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={
                "result": "false",
                "error_type": None,
                "error_message": "Not authenticated",
            },
        )
    user = await _get_user_by_id(session=session, id_=uid)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "result": "false",
                "error_type": None,
                "error_message": "User not found",
            },
        )
    response_following, response_follower = await _get_follower_and_following_by_user(
        session=session, user_in=user
    )
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "result": "true",
            "user": {
                "id": user.id,
                "name": user.name,
                "followers": response_follower,
                "following": response_following,
            },
        },
    )


@v1.post("/{uid}/follow")
async def follow_user(uid: int, api_key: str, session=Depends(get_db)) -> JSONResponse:
    par_user = await _get_user_by_key(session=session, api_key=api_key)
    if not par_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={
                "result": "false",
                "error_type": None,
                "error_message": "Not authenticated",
            },
        )
    user = await _get_user_by_id(session=session, id_=uid)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "result": "false",
                "error_type": None,
                "error_message": "User not found",
            },
        )
    follow_result = await _follow_user(
        following_uid=par_user.id, follower_uid=user.id, session=session
    )
    if not follow_result:
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
