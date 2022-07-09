from flask import g #Context object
import sqlite3

DATABASE_URL = "user_crud.db"

def get_db():
    db = getattr(g, "_database", None) #Checks if we have a connection 
    if not db:
        db = g._database = sqlite3.connect(DATABASE_URL)
    return db