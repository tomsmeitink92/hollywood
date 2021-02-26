from sqlalchemy import Column, String, Integer, ForeignKey, Table
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship
from config import Base


# Association table which links films to actors
films_actors_association = Table(
    "films_actors",
    Base.metadata,
    Column("film_id", Integer, ForeignKey("films.id")),
    Column("actor_id", Integer, ForeignKey("actors.id"))
)

# Association table which links films to directors
films_directors_association = Table(
    "films_directors",
    Base.metadata,
    Column("film_id", Integer, ForeignKey("films.id")),
    Column("director_id", Integer, ForeignKey("directors.id"))
)


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
    release_year = Column(Integer, nullable=False)
    genre = Column(String)

    # Relationship tables
    actors = relationship(
        "Actor",
        secondary=films_actors_association,
        back_populates="films"
    )
    directors = relationship(
        "Director",
        secondary=films_directors_association,
        back_populates="films"
    )

    def __init__(self, title: str, release_year: int, genre: str):
        self.title = title
        self.release_year = release_year
        self.genre = genre

    def __eq__(self, other):
        return self.title == other.title

    def __hash__(self):
        return hash(self.title)


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
    films = relationship(
        "Film",
        secondary=films_actors_association,
        back_populates="actors"
    )

    def __init__(self, name: str):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)


class Director(Base):
    __tablename__ = "directors"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    films = relationship(
        "Film",
        secondary=films_directors_association,
        back_populates="directors"
    )

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)


if __name__ == '__main__':
    from config import engine
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
