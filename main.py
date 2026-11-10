from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello():
    return {"message": "Привет, FastAPI!"}


@app.get("/greet")
def greet(name: str):
    return {"message": f"Привет, {name}!"}