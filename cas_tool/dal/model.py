from dataclasses import dataclass
from datetime import datetime


@dataclass
class TvShow:
    name: str
    year: datetime.date.year
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
