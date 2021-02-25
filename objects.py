from sqlalchemy import Column, String, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship
from config import Base


# Association table which links films to actors
film_actor = Table(
    "film_actor",
    Base.metadata,
    Column("film_id", Integer, ForeignKey("films.id")),
    Column("actor_id", Integer, ForeignKey("actors.id")))


class Film(Base):
    """
    :param id: Unique identification number.
    :type id: int
    :param title: Title of the film.
    :type title: str
    :param director: Name of the director of the film.
    :type director: str
    :param year: Publication year of the film.
    :type year: str
    """
    # Table name as presented in PostgreSQL
    __tablename__ = "films"

    # Field names
    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True)
    director = Column(String)
    year = Column(Integer)

    # Relationship tables
    actors = relationship("Actor", secondary=film_actor, back_populates="films")


class Actor(Base):
    """
    :param id: Unique identification number.
    :type id: int
    :param name: Name of the actor.
    :type name: str
    """
    # Table name as presented in PostgreSQL
    __tablename__ = "actors"

    # Field names
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    # Relationship tables
    films = relationship("Film", secondary=film_actor, back_populates="actors")


if __name__ == '__main__':
    from config import engine
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
