from etl.runner import ETL
from sal.storage.s3.services import S3DataService
from sal.storage.local.services import LocalStorageService
from sal.db_ops import services, uows 
from configure import settings
from uuid import uuid4, UUID

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
    process = ETL(data_service, services, storage_service, uow)

    try:
        entities = process.extract("tv_sample.csv")
        entities = process.transform(entities)
        for i, entity in entities.iterrows():
    
            print(f"trying to add entity: {i}")
            print(f"entity structure: {entity.to_dict()}")
            services.save_record(entity.to_dict(), uow)
            if i > 0:
                break


    except Exception as e:
        print(f"error occurred: {e}")


def aux_run():
    pass


if __name__ == "__main__":
    run()
