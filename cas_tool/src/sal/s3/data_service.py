import io
import boto3
import pandas as pd
from io import StringIO

class S3DataService:
    def __init__(self, endpoint_url, access_key, secret_key, bucket_name):
        self.client = boto3.client(
            's3',
            endpoint_url=endpoint_url,
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
            print(f"fetched  object: {object}")

        #response = self.client.get_object(Bucket=self.bucket_name, Key=file_key)
        #content = response['Body'].read().decode('utf-8')
        #data = StringIO(content)
        #df = pd.read_csv(data)
        #return df
        

    def read_excel(self, file_key:str, **kwargs):
        return pd.read_excel(io.BytesIO(self.get_response(file_key)['Body'].read()), **kwargs)