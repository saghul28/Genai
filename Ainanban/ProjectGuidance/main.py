from fastapi import FastAPI
from pydantic import BaseModel
import abstract

app = FastAPI()

app.include_router(abstract.router,prefix='/abstract',tags=["abstract"])

@app.get('/')
def home():
    return "<h1> Sample </h1>"