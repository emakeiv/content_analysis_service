import os
import pandas as pd


class LocalStorageService:
    def __init__(self, source_path, destination_path):
        self.path = source_path
        self.destination = destination_path
        if not os.path.exists(self.path):
            raise Exception(f"path {self.path} does not exist")
        if not os.path.isdir(self.path):
            raise Exception(f"path {self.path} is not a directory")
        if not os.listdir(self.path):
            raise Exception(f"path {self.path} is empty")

        self.files = [
            file
            for file in os.listdir(self.path)
            if os.path.isfile(os.path.join(self.path, file))
        ]
        if not self.files:
            raise Exception(f"path {self.path} is empty")

        self.file_formats = [
            file.split(".")[-1] for file in self.files if "." in file
        ]

        if not self.file_formats:
            raise Exception(f"path {self.path} does not contain any files")

    def read_file(self, file_name):
        file =  pd.read_csv(self.locate_file(file_name))
        return file

    def locate_file(
        self,
        file_name,
    ):
        return os.path.join(self.path, f"{file_name}")
