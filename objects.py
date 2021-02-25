from sqlalchemy import Column, String, Integer
from config import base


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
    from crud import session_scope
    with session_scope() as s:
        base.metadata.create_all(s)
