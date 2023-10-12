from typing import Annotated

from fastapi import APIRouter, Depends, Header, HTTPException, status
from fastapi.responses import JSONResponse

from apps.user.utils import (
    _follow_user,
    _get_follower_and_following_by_user,
    _get_user_by_id,
    _unfollow_user,
    get_user_by_key,
)
from apps.user.serializers import UserOut, UserIn, UserInDB
from apps.user.models import User
from core.db.database import get_db
from core.security.auth_security import get_password_hash

v1 = APIRouter()


@v1.get(path="/me")
async def get_me(
    api_key: Annotated[str | None, Header()], session=Depends(get_db)
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


@v1.post("/users", response_model=UserOut)
async def add_user(
    user: UserIn, session: object = Depends(get_db)
) -> User:
    hash_pass = get_password_hash(user.password)
    new_user = UserInDB(
        name=user.name,
        username=user.username,
        email=user.email,
        hashed_password=hash_pass,
        is_active=1
    )
    user = User(**new_user.dict())
    async with session.begin():
        session.add(user)
    return user


@v1.get("/{uid}")
async def get_user(
    uid: int, api_key: Annotated[str | None, Header()], session=Depends(get_db)
) -> JSONResponse:
    if not await get_user_by_key(session=session, api_key=api_key):
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
async def follow_user(
    uid: int, api_key: Annotated[str | None, Header()], session=Depends(get_db)
) -> JSONResponse:
    par_user = await get_user_by_key(session=session, api_key=api_key)
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
        status_code=status.HTTP_201_CREATED,
        content={"result": "true"},
    )


@v1.delete("/{uid}/follow")
async def unfollow_user(
    uid: int, api_key: Annotated[str | None, Header()], session=Depends(get_db)
) -> JSONResponse:
    par_user = await get_user_by_key(session=session, api_key=api_key)
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
    unfollow_result = await _unfollow_user(
        following_uid=par_user.id, follower_uid=user.id, session=session
    )
    if not unfollow_result:
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
