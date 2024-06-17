import io
import boto3
import pandas as pd
from io import StringIO

class S3DataService:
    def __init__(self, access_key, secret_key, bucket_name):
        self.client = boto3.client(
            's3',
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            region_name='eu-north-1'
        )
        self.bucket_name = bucket_name


    def read_csv(self, object_key:str):
        try:
            object = self.client.get_object(Bucket=self.bucket_name, Key=object_key)
        except Exception as e:
            print(f"Error reading key {object_key} from bucket {self.bucket_name}: {e}")
        else:
            print(f"successfully read key {object_key} from bucket {self.bucket_name}")
            content = object['Body'].read().decode('utf-8')
            data = StringIO(content)
            df = pd.read_csv(data)
            return df
        