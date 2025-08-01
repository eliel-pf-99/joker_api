import random
from sqlalchemy import func, select
from dto import JokeModel
from models import Joke, create_db

class DBJoke:
    def __init__(self):
        self.db = create_db()

    def count_jokes(self):
        statement = select(func.count(Joke.id)) # type: ignore
        row_count = self.db.exec(statement).one() # type: ignore
        return row_count[0]

    def getRandomJoke(self):
        jokeId = random.randint(1, self.count_jokes())
        joke = self.db.get(Joke, jokeId)
        return {'joke': joke}
        

    def createJoke(self, jokeModel: JokeModel):
        joke = Joke(
            setup=jokeModel.setup,
            delivery=jokeModel.delivery
        )
        self.db.add(joke)
        self.db.commit()
        return joke

    def denounceJoke(self, jokeId: int):
        joke = self.db.get(Joke, jokeId)

        if joke == None:
            return {'message': 'piada não encontrada'}
        
        joke.denounce += 1

        self.db.add(joke)
        self.db.commit()
        self.db.refresh(joke) 

        if joke.denounce > 4:
            self.deleteJoke(jokeId)

        return {'denounce times': joke.denounce}
    
    def deleteJoke(self, jokeId: int):
        joke = self.db.get(Joke, jokeId)
        self.db.delete(joke)
        self.db.commit()
        
