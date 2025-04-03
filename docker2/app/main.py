
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}
#http://127.0.0.1/
#output is {"Hello":"World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

#http://127.0.0.1/items/5?q=priya
#output is {"item_id":5,"q":"priya"}
#docker buildx build . -t {name of the image}
#docker run -d --name {container name}-p 8000:80 {name of the image}
#coverage run -m pytest or coverage run {name of the unit script}
#docker run -d --name {container name} -p 8000:80 {name of the image}
#docker ps -a --> list all the containers