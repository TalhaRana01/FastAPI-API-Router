from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_products():
  return {"data" : " All Products"}

@router.get("/{product_id}")
async def get_product(product_id: int):
  return {"data" : " Single Product"}