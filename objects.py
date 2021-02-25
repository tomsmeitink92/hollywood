from sqlalchemy import Column, String, Integer
from config import Base


class Film(Base):
    __tablename__ = "films"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    director = Column(String)
    year = Column(Integer)
    actor_id = Column(String)


class Actor(Base):
    __tablename__ = "actors"

    id = Column(Integer, primary_key=True)
    name = Column(String)


if __name__ == '__main__':
    from config import engine
    Base.metadata.create_all(engine)

