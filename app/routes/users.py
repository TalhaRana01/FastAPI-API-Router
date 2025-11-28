from fastapi import APIRouter

router = APIRouter()


@router.get("/users",tags=["Users"] )
async def get_users():
  return {"data" : " All Users"}

@router.get("/users/{user_id}", tags=["Users"])
async def get_user(user_id : int):
  return {"data" : "Single User"}