from fastapi import FastAPI
from typing import Optional

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


sdad




