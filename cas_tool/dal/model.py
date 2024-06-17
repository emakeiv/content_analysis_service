from dataclasses import dataclass

@dataclass
class TvShowData:
    asset_id: int
    duration: float
    name: str
    season: float
    episode: float
    description: str
    year: float
    actors: str
    director: str
    country: str
    content_type: str
    imdbid: str
    genre: str

    def __repr__(self):
        return f"TvShowData(asset_id={self.asset_id}, duration={self.duration}, name={self.name}, season={self.season}, episode={self.episode}, description={self.description}, year={self.year}, actors={self.actors}, director={self.director}, country={self.country}, content_type={self.content_type}, imdbid={self.imdbid}, genre={self.genre})"
    
    def __hash__(self) -> int:
        pass

    def __eq__(self, value: object) -> bool:
        pass