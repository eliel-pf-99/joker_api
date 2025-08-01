from pydantic import BaseModel

class JokeModel(BaseModel):
    setup: str
    delivery: str

class JokeId(BaseModel):
    id: int