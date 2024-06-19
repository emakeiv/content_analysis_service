from pydantic import BaseModel


class Show(BaseModel):
    name: str
    season: int
    episode: int
    duration: int
    imdbid: str
    actors: str
    director: str
    country: str
    content_type: str
    genre: str
    year: int
    description: str

    def dict(self):
        return {
            "name": self.name,
            "season": self.season,
            "episode": self.episode,
            "duration": self.duration,
            "imdbid": self.imdbid,
            "actors": self.actors,
            "director": self.director,
            "country": self.country,
            "content_type": self.content_type,
            "genre": self.genre,
            "year": self.year,
            "description": self.description,
        }
