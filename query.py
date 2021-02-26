from sqlalchemy import func
from objects import Actor, Film
from crud import session_scope

# Regular join query
with session_scope() as s:
    results = s.query(Film, Actor).join(Actor, Film.actors).filter(Film.title == "Fight Club")
    for film, actor in results:
        print(film.title, actor.name)

# Group by query
with session_scope() as s:
    result = s.query(Film.title, func.count(Actor.name)).join(Actor, Film.actors).group_by(Film.title)
    print(result)
    print(result.all())
