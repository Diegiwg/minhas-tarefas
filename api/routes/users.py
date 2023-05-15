from fastapi import APIRouter

from ..data import api
from ..models.user import UserCreate

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/")
async def create_user(user: UserCreate) -> dict:
    return api.create_user(user)
