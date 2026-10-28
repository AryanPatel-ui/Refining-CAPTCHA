
from fastapi import FastAPI

app = FastAPI(title="My First API")


@app.get("/")
def home():
    return {"message": "Hello, FastAPI!"}


@app.get("/about")
def about():
    return {
        "project": "My First FastAPI Project",
        "status": "running"
    }
