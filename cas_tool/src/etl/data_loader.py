from src.sal.s3.data_service import S3DataService

from configure import settings

primary_config = {
    "endpoint_url": settings.aws_s3_url,
    "access_key": settings.aws_access_key_id,
    "secret_key": settings.aws_secret_access_key,
    "bucket_name": settings.aws_s3_bucket
}

def init_s3_service():
    service = S3DataService(**primary_config)
    return service

    