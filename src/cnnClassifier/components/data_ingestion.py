import os
import urllib.request as request
import zipfile

from pathlib import Path
from cnnClassifier.entity.config_entity import DataIngestionConfig
from cnnClassifier.utils.common import get_size
from cnnClassifier import logger

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            logger.info(f"Downloading data from {self.config.source_URL}")
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
                )
            logger.info(f"Downloaded file: {filename} with headers: \n{headers}")
        else:
            logger.info(f"Data file already exists at {self.config.local_data_file}. Size: {get_size(Path(self.config.local_data_file))}")

    def extract_zip_file(self):
        os.makedirs(self.config.unzip_dir, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(self.config.unzip_dir)
            logger.info(f"Extracted files to {self.config.unzip_dir}")