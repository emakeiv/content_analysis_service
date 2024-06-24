from etl.runner import ETL
from sal.storage.s3.services import S3DataService
from sal.storage.local.services import LocalStorageService
from sal.db_ops import services as database_service
from sal.db_ops import uows
from configure import settings

s3_config = {
    "access_key": settings.aws_access_key_id,
    "secret_key": settings.aws_secret_access_key,
    "bucket_name": settings.aws_s3_bucket,
}

local_config = {
    
    "source_path": "data/raw/",
    "destination_path": "",
}

def run():

    data_service = S3DataService(**s3_config)
    storage_service = LocalStorageService(**local_config)
    uow = uows.DatabaseUnitOfWork()
    process = ETL(
        data_service, 
        database_service, 
        storage_service, 
        uow
    ) 

    try:
        d = process.extract("tv_sample.csv")
        
        process.transform(d)
        if process.validate(d):
            
            process.load_many(d)
            #process.load()
        else:
            print("validation failed")
        #process.load()
    except Exception as e:
        print(f"error occurred: {e}")

def aux_run():
    pass

if __name__ == "__main__":
    run()
