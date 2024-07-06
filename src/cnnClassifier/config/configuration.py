from cnnClassifier import logger
from cnnClassifier.constant import *
from cnnClassifier.utils.common import read_yaml, create_directories
from cnnClassifier.entity.config_entity import DataIngestionConfig

class ConfigurationManager:
    def __init__(self, config_filepath: Path=CONFIG_FILE_PATH, params_filepath: Path=PARAMS_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:

        data_ingestion_config = self.config.data_ingestion
        create_directories([data_ingestion_config.root_dir])

        return DataIngestionConfig(
            root_dir=data_ingestion_config.root_dir,
            source_URL=data_ingestion_config.source_URL,
            local_data_file=data_ingestion_config.local_data_file,
            unzip_dir=data_ingestion_config.unzip_dir
        )
