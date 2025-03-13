from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from models import Note, Description, Base  # Import Base from your model.py

# Database setup

engine = create_engine("sqlite:///notes.db")
SessionLocal = sessionmaker(bind=engine)

# Create the tables in the database
Base.metadata.create_all(engine)  # This will create the tables in the database if they don't exist

