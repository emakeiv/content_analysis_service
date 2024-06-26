from cas_tool.etl.transformations import ops

class ETL:
    def __init__(self, data_service, db_service, storage_service, uow):

        self.data_service = data_service
        self.db_service = db_service
        self.storage_service = storage_service
        self.uow = uow

    def extract(self, target):
        file = self.storage_service.read_file(target)
        # sfile = self.data_service.read_file(target)
        return file

    def load(self, data):
        save_to_db = self.db_service.save_record(data, self.uow)
        # save_to_file = self.storage_service.save_to_file(data)

    def load_many(self, data):
        self.db_service.save_many_records(data, self.uow)

    def transform(self, obj):
        """
        DONE:
            - handle missing values.
        TODO:
            - apply some data imputation techniques
            - normalize categorical columns.
            - parse and clean the 'description' field.
            - fix column dtypes
        """
        obj = ops.fillna(obj)
        obj = ops.types(obj)
        return obj
