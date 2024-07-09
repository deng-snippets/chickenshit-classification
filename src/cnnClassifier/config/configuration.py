from cnnClassifier import logger
from cnnClassifier.constant import *
from cnnClassifier.utils.common import read_yaml, create_directories
from cnnClassifier.entity.config_entity import DataIngestionConfig, PrepareBaseModelConfig

class ConfigurationManager:
    def __init__(self, config_filepath: Path=CONFIG_FILE_PATH, params_filepath: Path=PARAMS_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:

        create_directories([self.config.data_ingestion.root_dir])
        return DataIngestionConfig(
            root_dir=self.config.data_ingestion.root_dir,
            source_URL=self.config.data_ingestion.source_URL,
            local_data_file=self.config.data_ingestion.local_data_file,
            unzip_dir=self.config.data_ingestion.unzip_dir
        )
    
    def get_prepare_base_model_config(self):

        create_directories([self.config.prepare_base_model.root_dir])
        return PrepareBaseModelConfig(
            root_dir = Path(self.config.artifacts_root),
            base_model_path = Path(self.config.prepare_base_model.base_model_path),
            updated_base_model_path = Path(self.config.prepare_base_model.updated_base_model_path),
            params_image_size = self.params.IMAGE_SIZE,
            params_learning_rate = self.params.LEARNING_RATE,
            params_include_top = self.params.INCLUDE_TOP,
            params_weights = self.params.WEIGHTS,
            params_classes = self.params.CLASSES
        )
