from sqlalchemy import Column
from config import base, engine


class Film(base):
    __tablename__ = "films"

    title = Column()
    director = Column()
    year = Column()
    actor = Column()


class Actor(base):
    __tablename__ = "actors"


if __name__ == '__main__':
    from sqlalchemy.orm import Session

    session = Session(engine)
    base.metadata.create_all(engine)
