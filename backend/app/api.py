
from fastapi import FastAPI
from app.products.router import router as products_router
from app.categories.router import router as categories_router

app = FastAPI()

app.include_router(products_router, prefix="/products", tags=["products"])
app.include_router(categories_router, prefix="/categories", tags=["categories"])