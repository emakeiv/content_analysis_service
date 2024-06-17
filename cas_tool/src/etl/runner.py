import pandas as pd

class ETL:
    def __init__(self, service):
        print(type(service))
        self.data_service = service

    def extract(self, data_target):
        file = self.data_service.read_csv(data_target)
        return file

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        TODO:
            - apply some data imputation techniques
            - handle missing values.
            - normalize categorical columns.
            - parse and clean the 'description' field.
            - fix column dtypes
        """

        """
        range index: 366933
        default memory usage: 36.4+ MB
        column_type: {
            'asset_id: int64', 
            'duration: float64', 
            'name: object', 
            'season: float64', 
            'episode: float64', 
            'description: object', 
            'year: float64', 
            'actors: object', 
            'director: object', 
            'country: object', 
            'content_type: object', 
            'imdbid: object',
            'genre: object'
        }
        """

        df.fillna({
            'duration': 0,
            'name': '',
            'season': 0,
            'episode': 0,
            'description': '',
            'year:': '',
            'actors': '',
            'director': '',
            'country': 'unknown',
            'imdbid': 'unknown',
            'genre': 'unknown'
        }, inplace=True)

    def load(self):
        """
            TODO:
                - write data to a database.
        """
        pass