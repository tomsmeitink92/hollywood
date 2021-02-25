from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

host = getenv("host")
usr = getenv("user")
pwd = getenv("password")
db = getenv("database")

db_string = f"postgres://{usr}:{pwd}@{host}/{db}"
engine = create_engine(db_string)
base = declarative_base()
