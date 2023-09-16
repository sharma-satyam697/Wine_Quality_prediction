from src.mlproject import logger
from src.mlproject.config.configuration import ConfigurationManager
from src.mlproject.components.data_ingestion import DataIngestion



STAGE_NAME = 'Data Ingestion stage'

class DataIngestionTrainingPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config = data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
        
if __name__ == '__main__':
    try:
        logger.info(">>>>>Stage {} started".format(STAGE_NAME))
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(">>>> stage {} completed".format(STAGE_NAME))
    
    except Exception as e:
        logger.exception(e)
        raise e
        


