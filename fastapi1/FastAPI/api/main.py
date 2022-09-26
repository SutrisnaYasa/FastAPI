from fastapi import FastAPI, status
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

@app.post('/articles/', status_code=status.HTTP_201_CREATED)
def add_article(article:ArticleSchema, db:Session = Depends(get_db)):
    new_article = models.Article(title=article.title, description=article.description)
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article
