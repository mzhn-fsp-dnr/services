"""Database configuration."""

from functools import lru_cache
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from . import config


@lru_cache()
def get_settings():
    """
    Config settings function.
    """
    return config.Settings()


conf_settings = get_settings()
database_url = conf_settings.database_link()

engine = create_engine(database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency
def get_db():
    """
    Gets database session.
    """
    db_session = SessionLocal()
    try:
        yield db_session
    finally:
        db_session.close()
