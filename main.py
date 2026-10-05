from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"status": "alive"}


@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello, {name}"}