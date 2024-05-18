from fastapi import FastAPI , Depends , status , Response , HTTPException
from pydantic import BaseModel
import schemas , models 
# from blog.database import engine
# from .database import engine , SessionLocal
from database import SessionLocal , engine , Base
from sqlalchemy.orm import Session
import pprint


app = FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal() 
    try:
        yield db
    finally:
        db.close()




@app.post("/blog" , status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog , db : Session = Depends(get_db)):
    new_blog = models.Blog(title = request.title , body = request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.get('/blog')
def all(db:Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@app.get('/blog/{id}')
def show(id , response : Response, db:Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND , detail = f"Blog with the id {id}  not available")
         
    
    return blog


@app.delete('/blog/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy(id,db:Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)




x = globals()
pprint.pprint(x)