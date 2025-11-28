from fastapi import FastAPI
from app.routes.users import router as user_routers
from app.routes.products import router as product_routers

app = FastAPI()


# app.include_router(user_routers)
app.include_router(product_routers)


