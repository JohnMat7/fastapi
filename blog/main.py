from fastapi import FastAPI
from pydantic import BaseModel
import schemas , models 
# from blog.database import engine
import database

app = FastAPI()

models.database.Base.metadata.create_all(database.engine)


@app.post("/blog")
def create(request: schemas.Blog):
    return request



