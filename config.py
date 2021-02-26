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

# Define the connection string used to connect to our PostgreSQL database
db_string = f"postgres://{usr}:{pwd}@{host}/{db}"

# Create the search engine for SQLAlchemy
engine = create_engine(db_string)

# Add a declarative base class, to be inherited by our models/objects
Base = declarative_base()

# Define a session, which "manages persistence operations for ORM-mapped objects"
session = Session(engine)
