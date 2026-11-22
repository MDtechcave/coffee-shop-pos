#Database Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from app.core.config import settings

#establishes the database connection
engine = create_engine(
    settings.DATABASE_URL,
    echo=True
)
#creates database sessions
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
#foundation for our database models
Base = declarative_base()

#provides database sessions to our API endpoints and closes them afterwards
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()