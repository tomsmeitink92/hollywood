from crud import session_scope
from objects import Actor, Film


actors = [
    Actor(name="Brad Pitt"),
    Actor(name="Kevin Spacey"),
    Actor(name="Morgan Freeman")
]
films = [
    Film(title="Se7en", director="David Fincher", year=1995),
    Film(title="Fight Club", director="David Fincher", year=1999)
]
for actor in actors:
    films[0].actors.append(actor)
films[1].actors.append(actors[0])


with session_scope() as s:
    s.add_all(actors)
    s.add_all(films)
