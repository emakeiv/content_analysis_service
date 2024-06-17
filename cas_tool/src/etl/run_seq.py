

from src.etl.data_loader import init_s3_service

def extract():
    pass

def transform():
    pass

def load():
    long_key = 's3://tv-show-records/tv_sample.csv'
    short_key = 'tv_sample.csv'
    data_service = init_s3_service()
    file = data_service.read_csv(long_key)
    print(file)