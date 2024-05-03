from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"data" : {"name" : "messi"}}


@app.get("/about")
def about():
    return "this is about section"