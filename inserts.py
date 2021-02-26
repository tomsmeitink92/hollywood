from dataset import load_data
from crud import session_scope
from objects import Actor, Film

# Get data from excel file
df = load_data()
df["Leading actors"] = df["Leading actors"].str.replace(" and ", ", ")
df["actors"] = df["Leading actors"].str.split(", ")
df.dropna(subset=["actors"], inplace=True)

# Initialize the objects
actors = {actor for actor_list in df["actors"] for actor in actor_list}
actors = {name: Actor(name=name) for name in actors}

films = []
for idx, row in df.iterrows():
    film = Film(
        title=row["Film"],
        director=row["Director"],
        release_year=row["Year of cinema release"],
        genre=row["genre"]
    )
    for actor in row["actors"]:
        film.actors.append(actors[actor])
    films.append(film)

# Commit the data to PostgreSQL
with session_scope() as s:
    s.add_all(films)
