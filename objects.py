from sqlalchemy import Column, String, Integer
from config import base, engine


class Film(base):
    __tablename__ = "films"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    director = Column(String)
    year = Column(Integer)
    actor_id = Column(String)


class Actor(base):
    __tablename__ = "actors"

    id = Column(Integer, primary_key=True)
    name = Column(String)


if __name__ == '__main__':
    from sqlalchemy.orm import Session

    session = Session(engine)
    base.metadata.create_all(engine)
