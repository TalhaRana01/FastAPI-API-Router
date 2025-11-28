from fastapi import FastAPI

app = FastAPI()


@app.get("/users")
async def get_users():
  return {"data" : " All Users"}

@app.get("/users/{user_id}")
async def get_user(user_id : int):
  return {"data" : "Single User"}


@app.get("/products")
async def get_products():
  return {"data" : " All Products"}

@app.get("/products/{product_id}")
async def get_product(product_id: int):
  return {"data" : " Single Product"}