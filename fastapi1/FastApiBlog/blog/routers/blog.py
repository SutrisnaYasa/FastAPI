from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
import schemas, database, models
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/blog",
    tags=['Blogs']
)
get_db = database.get_db

@router.get('/', response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with id {id} not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with id {id} is not found")
    blog.update(request.dict())
    db.commit()
    return 'updated'

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def show(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not available")
    return blog


# @app.get('/blog', response_model=List[schemas.ShowBlog], tags=['Blogs'])
# def all(db: Session = Depends(get_db)):
#     blogs = db.query(models.Blog).all()
#     return blogs


# @router.get('/blog/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog, tags=['Blogs'])
# def show(id, response: Response, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id).first()
#     if not blog:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not available")
#         # response.status_code = status.HTTP_404_NOT_FOUND
#         # return {'detail':f"Blog with the id {id} is not available"}
#     return blog

