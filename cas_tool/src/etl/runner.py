

class ETL:
    def __init__(self, service):
        print(type(service))
        self.data_service = service

    def extract(self, data_target):
        file = self.data_service.read_csv(data_target)
        return file

    def transform(self):
        """
        TODO:
            - handle missing values.
            - normalize categorical columns.
            - parse and clean the 'description' field.
        """
        pass

    def load(self):
        """
            TODO:
                - write data to a database.
        """
        pass