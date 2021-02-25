from sqlalchemy import Column, String, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship
from config import Base


# class FilmActor(Base):
#     __tablename__ = 'film_actor'
#
#     id = Column(Integer, primary_key=True)
#     film_id = Column(Integer, ForeignKey('films.id'), primary_key=True)
#     actor_id = Column(Integer, ForeignKey('actors.id'), primary_key=True)
#
#     actor = relationship("Actor", backref="film_actor")
#     film = relationship("Film", backref="film_actor")

film_actor = Table(
    "film_actor",
    Base.metadata,
    Column("film_id", Integer, ForeignKey("films.id")),
    Column("actor_id", Integer, ForeignKey("actors.id")))


class Film(Base):
    __tablename__ = "films"

    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True)
    director = Column(String)
    year = Column(Integer)

    actors = relationship("Actor", secondary=film_actor, back_populates="films")


class Actor(Base):
    __tablename__ = "actors"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    films = relationship("Film", secondary=film_actor, back_populates="actors")


if __name__ == '__main__':
    from config import engine
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
