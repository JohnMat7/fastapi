from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

myapp = FastAPI()

@myapp.get("/blogs")
def index(limit=10 , published:bool = True , sort: Optional[str] = None):
    # return published  (to check what we getting for testing )
    if published :
        return {'data1' : f'{limit} published blogs from the db' }
    else: 
        return {"data" : f'{limit} blogs from db'}


@myapp.get("/blogs/unpublished")
def index():
    return {"unplublished blogs"}





@myapp.get("/blogs/{id}")
def about(id : int):
    #fetch blog with id = id
    return {"data" : id}

@myapp.get("/blogs/{id}/comments")
def comments(id:int , limit=10):
    return {"data" : {'1','2'}}


class Blog(BaseModel):
    title : str
    body : str
    published : Optional[bool]



@myapp.post("/blog")
def create_blog(blog: Blog):
    return {"data":f"Blog is created with title as {blog.title}" }


if __name__ == "__main__":
    uvicorn.run(myapp,host="127.0.0.1",port=9000)