from pydantic import BaseModel, Field
from typing import List
from uuid import uuid4, UUID


class TvShowRecordSchema(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    asset_id: int
    name: str
    year: int
    season: int
    episode: int
    duration: float
    imdbid: str
    actors: str
    director: str
    country: str
    content_type: str
    genre: str
    description: str


class TVShowRecordsListSchema(BaseModel):
    records: List[TvShowRecordSchema]
