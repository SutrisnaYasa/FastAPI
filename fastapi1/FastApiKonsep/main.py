from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()


@app.get('/')
def index():
    # return 'heyyy'
    # return {'data': {'name': 'Budi'}}
    return {'data': 'blog list'}


@app.get('/blog')
# def index(limit, published: bool):
def index(limit=10, published: bool = True, sort: Optional[str] = None):
    # only get 10 published blogs
    if published:
        return {'data': f'{limit} published blogs from the db'}
    else:
        return {'data': f'{limit} blogs from the db'}


@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blogs'}


@app.get('/about')
def about():
    return {'data': {'About Page'}}


@app.get('/blog/{id}')
def show(id):  # id nya default string
    # def show(id: int): #merubah id menjadi int
    # fetch blog with id = id
    return {'data': id}


@app.get('/blog/{id}/comments')
def comments(id):
    # fetch comments of blog with id = id
    return {'data': {'1', '2'}}


class Blog(BaseModel):
    # pass
    title: str
    body: str
    published: Optional[bool]


@app.post('/blog')
def create_blog(request: Blog):
    # return request
    # return {'data': "Blog is created"}
    return {'data': f"Blog is created with title as {request.title}"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9000)
    # runningnya => python3 main.py
