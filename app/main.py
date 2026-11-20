from fastapi import FastAPI

app = FastAPI(
    title="Coffee shop POS API",
    description= "Backend Api for managing coffee shop orders",
    version = "1.0.0"
)
@app.get("/")
def home():
    return {
        "message": "Welcome to Coffee shop Pos"
    }

@app.get ("/health")
def health_check():
    return {
        "status": "healthy"
    }
