import sqlite3
from fastapi import FastAPI

app =FastAPI()

conn = sqlite3.connect("mydatabase.db",check_same_thread=False)

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT,
               completed TEXT
               )


""")


conn.commit()

@app.get("/")
def home():
    return {
        "message" : "Welcome to FastAPI with SQLite"
    }