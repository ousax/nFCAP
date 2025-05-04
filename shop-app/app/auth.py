import sqlite3, bcrypt
from fastapi import APIRouter, Form, HTTPException

router = APIRouter()

def get_db():
    return sqlite3.connect("shop.db")

@router.post("/register")
def register(email: str = Form(...), password: str = Form(...)):
    hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    conn = get_db()
    try:
        conn.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, hashed_pw))
        conn.commit()
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=400, detail="L'email est déjà utilisé.")
    finally:
        conn.close()
    return {"message": "Inscription réussie!"}

@router.post("/login")
def login(email: str = Form(...), password: str = Form(...)):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE email = ?", (email,))
    row = cursor.fetchone()
    conn.close()
    if not row or not bcrypt.checkpw(password.encode(), row[0]):
        raise HTTPException(status_code=401, detail="Identifiants invalides.")
    return {"message": "Connexion réussie!"}

@router.post("/reset-password")
def reset_password(email: str = Form(...)):
    # This is a placeholder — you can later send a real email
    return {"message": f"Un lien de réinitialisation sera envoyé à {email} (simulation)."}

