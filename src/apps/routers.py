from fastapi import APIRouter

from apps.user.views import v1 as user_v1

router = APIRouter()

router.include_router(router=user_v1, prefix="/api/users", tags=["users"])
