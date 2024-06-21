from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from configure import settings

DEFAULT_SESSION_FACTORY = sessionmaker(bind=create_engine(settings.db_uri))
