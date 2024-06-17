
from src.etl.runner import ETL
from src.sal.s3.data_service import S3DataService
from configure import settings

primary_config = {
    "access_key": settings.aws_access_key_id,
    "secret_key": settings.aws_secret_access_key,
    "bucket_name": settings.aws_s3_bucket
}


def run():
    """
    runs the ETL extract, transformm load  process using an S3 data service as primary data source.
    This function extracts data from an S3 bucket, using the configuration settings
    provided in the `primary_config` dictionary. It then prints the head of the extracted data. 
    """


    data_service = S3DataService(**primary_config)
    process = ETL(data_service)
    try:
        data = process.extract("tv_sample.csv")
    except Exception as e:
        print(f"error occurred during data extract: {e}")
    else:
        print(f"data successfully extracted")
        print(data.head())

    # process.transform()
    # process.load()

if __name__ == "__main__":
    run()
    