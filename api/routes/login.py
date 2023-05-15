from fastapi import APIRouter

from ..data import api
from ..models.user import UserLogin

router = APIRouter(prefix="/login", tags=["users"])


@router.post("/")
def login(user: UserLogin):
    return api.login(user)
