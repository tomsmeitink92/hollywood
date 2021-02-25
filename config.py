from os import getenv
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

load_dotenv()

host = getenv("host")
usr = getenv("user")
pwd = getenv("password")
db = getenv("database")

db_string = f"postgres://{usr}:{pwd}@{host}/{db}"
engine = create_engine(db_string)
base = declarative_base()
session = Session(engine)
