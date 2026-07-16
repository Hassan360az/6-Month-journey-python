from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker

# Database Connection

DATABASE_URL = "postgresql://postgres:8776@localhost:5432/postgres"

engine = create_engine(DATABASE_URL)

# Base

Base = declarative_base()

# Session

SessionLocal = sessionmaker(bind=engine)
