from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from .models import Article_Pydantic, ArticleIn_Pydantic, Article
from tortoise.contrib.fastapi import HTTPNotFoundError, register_tortoise
from typing import List
from pydantic import BaseModel



app = FastAPI()


class Status(BaseModel):
    message:str

@app.get('/articles', response_model=List[Article_Pydantic])
async def get_article():
    return await Article_Pydantic.from_queryset(Article.all())

@app.get('/articles/{id}',response_model=Article_Pydantic, responses={404 :{"model":HTTPNotFoundError}})
async def get_details(id:int):
    return await Article_Pydantic.from_queryset_single(Article.get(id=id))


@app.post('/articles', response_model=Article_Pydantic)
async def insert_article(article:ArticleIn_Pydantic):
    article_obj = await Article.create(**article.dict(exclude_unset=True))
    return await Article_Pydantic.from_tortoise_orm(article_obj)


@app.put('/articles/{id}', response_model=Article_Pydantic, responses={404 :{"model":HTTPNotFoundError}})
async def update_Article(id:int, article:ArticleIn_Pydantic):
    await Article.filter(id=id).update(**article.dict(exclude_unset=True))
    return await Article_Pydantic.from_queryset_single(Article.get(id=id))

@app.delete('/articles/{id}', response_model=Status, responses={404 :{"model":HTTPNotFoundError}})
async def delete_article(id:int):
    deleted_article = await Article.filter(id=id).delete()

    if not deleted_article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail = f"Article {id} not found")
    
    return Status(message = f"Deleted Article {id}")



register_tortoise(
    app,
    db_url = "mysql://root:@localhost:3306/articleorm",
    modules={"models":["api.models"]},
    generate_schemas=True,
    add_exception_handlers=True
)
