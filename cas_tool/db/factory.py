from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DEFAULT_SESSION_FACTORY = sessionmaker(
    bind=create_engine(
        config.get_db_uri(),
    )
)