from fastapi import APIRouter

router = APIRouter()


@router.get("/users")
async def get_users():
  return {"data" : " All Users"}

@router.get("/users/{user_id}")
async def get_user(user_id : int):
  return {"data" : "Single User"}