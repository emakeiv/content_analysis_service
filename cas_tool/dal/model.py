from dataclasses import dataclass

@dataclass
class TvShow:
    id: str 
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
    
    def dict(self):
        return{
            "id": self.id,
            "asset_id": self.asset_id,
            "name": self.name,
            "year": self.year,
            "season": self.season,
            "episode": self.episode,
            "duration": self.duration,
            "imdbid": self.imdbid,
            "actors": self.actors,
            "director": self.director,
            "country": self.country,
            "content_type": self.content_type,
            "genre": self.genre,
            "description": self.description
        }

