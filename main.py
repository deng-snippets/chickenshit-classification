from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionPipeline

STAGE_NAME = 'Data Ingestion stage'

try:
    logger.info(f"Starting {STAGE_NAME}")
    pipeline = DataIngestionPipeline()
    pipeline.main()
    logger.info(f"Completed {STAGE_NAME}")
except Exception as e:
    logger.exception(e)
    raise e