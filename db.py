# Import necessary dependencies
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define SQLite connection url
SQLALCHEMY_DATABASE_URL = "sqlite:///./data-stored/api.db"

# Create engine instance 
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Create sessionmaker 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()