from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    environment: str
    pythonpath: str
    aws_access_key_id: str
    aws_secret_access_key: str
    aws_s3_bucket: str
    db_uri: str

    class Config:
        env_file = "./.env"
        env_file_encoding = "utf-8"


settings = Settings()
