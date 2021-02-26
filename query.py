from sqlalchemy import func, text
from models import Actor, Film, Director
from crud import session_scope

# Regular join query
with session_scope() as s:
    results = s.query(Film, Actor).join(Actor, Film.actors).filter(Film.title == "Fight Club")
    for film, actor in results:
        print(film.title, actor.name)

# Group by query: Group film with the largest cast
with session_scope() as s:
    result = (
        s.query(Film.title, func.count(Actor.name).label("count"))
        .join(Actor, Film.actors)
        .group_by(Film)
        .order_by(text("count DESC"))
        .limit(1)
        .all()
    )
    for title, count in result:
        print(title, count)

# Group by query: Group actor that has worked with the most directors
with session_scope() as s:
    result = (
        s.query(Actor.name, func.count(Director.name).label("count"))
        .join(Film, Actor.films)
        .join(Director, Film.directors)
        .group_by(Actor)
        .order_by(text("count DESC"))
        .limit(1)
        .all()
    )
    for actor, count in result:
        print(actor, count)
