from fastapi import FastAPI
from dbJoke import DBJoke
from dto import JokeModel


app = FastAPI()
db = DBJoke()

@app.get("/")
async def root():
    return {'message': 'Hello World!'}

@app.get("/getJoke")
async def getJoke():
    return db.getRandomJoke()

@app.patch("/denounceJoke")
async def denounceJoke(id: int):
    return db.denounceJoke(id)

@app.post("/createJoke")
async def createJoke(joke: JokeModel):
    return {'joke': db.createJoke(joke)}





