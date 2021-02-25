from crud import session_scope
from objects import Actor, Film


# Initialize the objects
actors = [
    Actor(name="Brad Pitt"),
    Actor(name="Kevin Spacey"),
    Actor(name="Morgan Freeman")
]
films = [
    Film(title="Se7en", director="David Fincher", year=1995),
    Film(title="Fight Club", director="David Fincher", year=1999)
]

# Append actors to films
for actor in actors:
    films[0].actors.append(actor)
films[1].actors.append(actors[0])


# Commit the data to PostgreSQL
with session_scope() as s:
    s.add_all(actors)
    s.add_all(films)
