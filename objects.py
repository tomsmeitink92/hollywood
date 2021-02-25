from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from config import Base


class FilmActor(Base):
    __tablename__ = 'film_actor'

    id = Column(Integer, primary_key=True)
    film_id = Column(Integer, ForeignKey('films.id'))
    actor_id = Column(Integer, ForeignKey('actors.id'))

    actor = relationship("Actor", back_populates="films")
    film = relationship("Film", back_populates="actors")


class Film(Base):
    __tablename__ = "films"

    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True)
    director = Column(String)
    year = Column(Integer)

    actors = relationship("FilmActor", back_populates="film")


class Actor(Base):
    __tablename__ = "actors"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    films = relationship("FilmActor", back_populates="actor")


if __name__ == '__main__':
    from config import engine
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
