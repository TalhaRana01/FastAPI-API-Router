from fastapi import APIRouter

router = APIRouter()


@router.get("/" )
async def get_users():
  return {"data" : " All Users"}

@router.get("/{user_id}")
async def get_user(user_id : int):
  return {"data" : "Single User"}