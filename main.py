from fastapi import FastAPI

myapp = FastAPI()

@myapp.get("/blogs")
def index(limit):
    return {"data" : f'{limit} blogs from db'}


@myapp.get("/blogs/unpublished")
def index():
    return {"unplublished blogs"}





@myapp.get("/blogs/{id}")
def about(id : int):
    #fetch blog with id = id
    return {"data" : id}

@myapp.get("/blogs/{id}/comments")
def comments(id:int):
    return {"data" : {'1','2'}}

