from  fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()

@app.get('/blog')
def index(limit=10, published:bool= True, sort: Optional[str] = None):
    
    if published:
       return {'data':f'{limit} published blog from db'}
    else:
        return {'data':f'{limit} 10 blog from db'}

@app.get('/blog/unpublished')
def unpublished():
     return {'data': 'unpublished blogs'}

@app.get('/blog/{id}')
def show(id:int):
     return {'data': id}


@app.get('/blog/{id}/comments')
def comments(id,limit=10):
    return{'data':{limit}}

class Blog(BaseModel):
    title: str
    body: str
    published_at: Optional[bool]

@app.post('/blog')
def create_blog(blog:Blog):
    return {'data':f"Blog is created with title as {blog.title}"}


#if__name__ =- "__main__":
#uvicorn.run(app, host="127.0.0.1", port=9000)