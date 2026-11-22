from fastapi import FastAPI
from sqlalchemy import text

from app.db.session import engine

app = FastAPI(
    title="Coffee shop POS API",
    description= "Backend Api for managing coffee shop orders",
    version = "1.0.0"
)
@app.get("/")
def home():
    return {
        "message": "Welcome to Coffee shop Pos API"
    }

@app.get ("/database-check")
def database_check():

    try: 
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

        return {
            "database": "Connected successfully"
        }

    except Exception as e:
        return {
            "database": "Connection failed",
            "error": str(e)
        }
