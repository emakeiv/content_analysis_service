

from dal.model import TvShow
from sqlalchemy.orm import registry
from sqlalchemy.schema import MetaData
from sqlalchemy import Table, Column, Integer, String, Float, ForeignKey


metadata = MetaData()
mapper_registry = registry(metadata=metadata)

tv_show_table = Table(
    "tv_show_records",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("asset_id", Integer),
    Column("name", String),
    Column("year", Integer),
    Column("season", Integer),
    Column("episode", Integer),
    Column("duration", Float),
    Column("imdbid", String),
    Column("actors", String),
    Column("director", String),
    Column("country", String),
    Column("content_type", String),
    Column("genre", String),
    Column("description", String),
)

def start_mappers():
    mapper_registry.map_imperatively(TvShow, tv_show_table)
