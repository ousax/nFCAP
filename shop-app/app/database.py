import sqlite3
def init_db():
    conn = sqlite3.connect("shop.db")
    cursor = conn.cursor()
    
    # Users table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)
    
    # Products table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            rating REAL DEFAULT 0,
            image_url TEXT,
            currency TEXT DEFAULT 'EUR'
        )
    """)
    
    conn.commit()
    conn.close()

