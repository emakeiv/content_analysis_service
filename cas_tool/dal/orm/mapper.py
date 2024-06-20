from sqlalchemy import Table, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import registry
from dal.model import TvShow


mapper_registry = registry()
metadata = mapper_registry.metadata

tv_show_records = Table(
    "tv_show_records",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("asset_id", Integer, ForeignKey("asset.id")),
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
    mapper_registry.map_imperatively(TvShow, tv_show_records)
