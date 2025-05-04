from fastapi import APIRouter
import sqlite3

router = APIRouter()

def get_db():
    return sqlite3.connect("shop.db")

@router.get("/")
def get_all_products():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, price, rating, image_url, currency FROM products")
    products = cursor.fetchall()
    conn.close()
    return [
        {
            "id": row[0],
            "name": row[1],
            "price": row[2],
            "rating": row[3],
            "image_url": row[4],
            "currency": row[5]
        }
        for row in products
    ]

