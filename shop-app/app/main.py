from fastapi import FastAPI
from app import auth, database, products
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Boutique en Ligne")

database.init_db()

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(products.router, prefix="/products", tags=["products"])
app.mount("/static", StaticFiles(directory="static"), name="static")

