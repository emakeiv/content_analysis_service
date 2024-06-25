class ETL:
    def __init__(self, data_service, db_service, uow):
    
        self.data_service = data_service
        self.db_service = db_service
        self.storage_service = storage_service
        self.uow = uow

    def extract(self, target):
        file = self.data_service.reaf_file(target)
        return file

    def load(self, data):
        save_to_db = self.db_service.save_many_records(data, self.uow)
        

    def transform(self, obj):
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
     
        obj.fillna(
            {
                "duration": 0,
                "name": "",
                "season": 0,
                "episode": 0,
                "description": "",
                "year:": 0,
                "actors": "",
                "director": "",
                "country": "unknown",
                "content_type": "unknown",
                "imdbid": "unknown",
                "genre": "unknown",
            },
            inplace=True,
        )
     
        return obj
        

        
