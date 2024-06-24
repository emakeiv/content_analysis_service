import io
import boto3
import pandas as pd
from io import StringIO

#TODO: uow patern impl
#TODO: generic data service interface

class S3DataService:
    def __init__(self, access_key, secret_key, bucket_name, region_name="eu-north-1"):
        self.client = boto3.client(
            "s3",
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            region_name=region_name,
        )
        self.bucket_name = bucket_name

    def read_file(self, object_key: str):
        try:
            object = self.client.get_object(Bucket=self.bucket_name, Key=object_key)
        except Exception as e:
            print(
                f"error reading key {object_key} from bucket {self.bucket_name}: {e}"
            )
        else:
            print(
                f"successfully read key {object_key} from bucket {self.bucket_name}"
            )
            content = object["Body"].read().decode("utf-8")
            data = pd.read_csv(StringIO(content))
            return data

 