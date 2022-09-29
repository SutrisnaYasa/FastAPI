from os import stat
from fastapi import FastAPI, status, HTTPException
from fastapi.params import Depends
from database import engine, sessionLocal
import models
from schemas import ArticleSchema, MyArticleSchema
from sqlalchemy.orm import Session
from typing import List


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/articles/', response_model=List[MyArticleSchema])
def get_article(db:Session = Depends(get_db)):
    myarticles = db.query(models.Article).all()
    return myarticles

@app.get('/articles/{id}', status_code=status.HTTP_200_OK, response_model= MyArticleSchema)
def article_details(id:int, db:Session = Depends(get_db)):
    #myarticle = db.query(models.Article).filter(models.Article.id == id).first()
    myarticle = db.query(models.Article).get(id)
    if myarticle:
        return myarticle
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The article does not exists")

@app.post('/articles/', status_code=status.HTTP_201_CREATED)
def add_article(article:ArticleSchema, db:Session = Depends(get_db)):
    new_article = models.Article(title=article.title, description=article.description)
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article

@app.put('/articles/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_article(id, article:ArticleSchema, db:Session = Depends(get_db)):
    db.query(models.Article).filter(models.Article.id == id).update({'title':article.title, 'description':article.description})
    return {"message":"The data is updated"}

@app.delete('/articles/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_article(id:int, db:Session = Depends(get_db)):
    db.query(models.Article).filter(models.Article.id == id).delete(synchronize_session=False)
    db.commit()
