from fastapi import FastAPI
from pydantic import BaseModel
import aptitude


app = FastAPI()

app.include_router(aptitude.router,prefix="/interview",tags=["apitude"])



@app.get('/')
def home():
    return "<h1> Sample </h1>"