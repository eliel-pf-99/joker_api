import random
from sqlalchemy import func, select
from dto import JokeModel
from models import Joke, do

class DBJoke:

    def random_joke(self):
        def action(eng):
            statement = select(Joke).order_by(func.random()).limit(1)
            joke = eng.exec(statement).first()  # type: ignore
            return joke
        joke_random = do(action)
        return joke_random
        
    def createJoke(self, jokeModel: JokeModel):
        joke = Joke(
            setup=jokeModel.setup,
            delivery=jokeModel.delivery
        )
        def action(eng):
            eng.add(joke)
            eng.commit()
        do(action)
        return joke

    def getJokeById(self, jokeId: int):
        def action(eng):
            joke = eng.get(Joke, jokeId)
            return joke or None
        return do(action)

    def denounceJoke(self, jokeId: int):
        joke = self.getJokeById(jokeId)

        if joke == None:
            return {'message': 'piada não encontrada'}
        
        joke.denounce += 1
        
        def action(eng):
            eng.add(joke)
            eng.commit()
            eng.refresh(joke)
        
        do(action)

        self.checkHowMuchDenounce(jokeId)

        return {'denounce times': joke.denounce}
    
    def checkHowMuchDenounce(self, jokeId: int):
        joke = self.getJokeById(jokeId)
        if joke == None: return

        if joke.denounce > 4:
            self.deleteJoke(joke)

    def deleteJoke(self, joke: Joke):
        def action(eng):
            eng.delete(joke)
            eng.commit()
        do(action)
        
