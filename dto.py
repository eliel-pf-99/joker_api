from pydantic import BaseModel

class JokeModel(BaseModel):
    setup: str
    delivery: str
