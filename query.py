from objects import Actor, Film
from crud import session_scope

with session_scope() as s:
    result = s.query(Film, Actor).join(Actor, Film.actors).filter(Film.title == "Fight Club")
    for film, actor in result:
        print(film.title, actor.name)
