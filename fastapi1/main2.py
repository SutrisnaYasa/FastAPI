from fastapi import FastAPI
# from pydantic import BaseModel


# class Article(BaseModel):
#     id:int
#     title:str
#     description:str

app = FastAPI()


# data = [
#     {"title":"First title"},
#     {"title":"Second title"},
#     {"title":"Third title"}
# ]


@app.get('/')
async def Index():
    return {"message":"Hello Boys"}


# @app.get('/articles/{id}')
# def get_article(id:int):
#     return {"article":{id}}

# @app.get('/articles/')
# def get_article(skip:int=0, limit:int=20):
#     return data[skip : skip + limit]


# @app.post('/article/')
# def add_article(article:Article):
#     return article
