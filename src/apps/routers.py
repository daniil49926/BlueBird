from fastapi import APIRouter

from apps.media.views import v1 as media_v1
from apps.tweet.views import v1 as tweet_v1
from apps.user.views import v1 as user_v1

router = APIRouter()

router.include_router(router=user_v1, prefix="/api/users", tags=["users"])
router.include_router(router=tweet_v1, prefix="/api/tweets", tags=["tweets"])
router.include_router(router=media_v1, prefix="/api/medias", tags=["medias"])
