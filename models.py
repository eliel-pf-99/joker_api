from sqlmodel import SQLModel, Field, create_engine, Session

import settings

class Joke(SQLModel, table=True):
    id: int | None = Field(primary_key=True, default=None)
    setup: str
    delivery: str
    denounce: int = Field(default=0)

def create_db():
    engine = create_engine(settings.settings.database_url)
    SQLModel.metadata.create_all(engine)
    
    with Session(engine) as session:
        return session
    
def do(action):
    engine = create_engine(settings.settings.database_url)
    SQLModel.metadata.create_all(engine)
    
    with Session(engine) as session:
        return action(session)

        
