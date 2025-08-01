from fastapi import FastAPI
from dbJoke import DBJoke
from dto import JokeId, JokeModel
from fastapi.middleware.cors import CORSMiddleware

db = DBJoke()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
async def root():
    return {'message': 'Hello World!'}

@app.get("/getJoke")
async def getJoke():
    return db.getRandomJoke()

@app.patch("/denounceJoke")
async def denounceJoke(id: JokeId):
    print(id)
    return db.denounceJoke(id.id)

@app.post("/createJoke")
async def createJoke(joke: JokeModel):
    return {'joke': db.createJoke(joke)}





