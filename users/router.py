from fastapi import APIRouter


router = APIRouter(
    prefix="/users",
    tags=["юзеры"],
)


@router.get("")
async def get_users():
    pass


@router.get("/{username_user}")
async def get_username_user(username_user: str):
    pass