from src.mlproject.config.configuration import ConfigurationManager
from src.mlproject.components.data_transformation import DataTransformation
from src.mlproject import logger

STAGE_NAME = 'Data Transformation stage'

class DataTransformationTrainingPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):       
        try:
            logger.info('Ready for transformation')
            config  =ConfigurationManager()
            data_transformation_config = config.get_data_transformation_config()
            data_transformation = DataTransformation(config=data_transformation_config)
            data_transformation.train_test_splitting()
            
        except Exception as e:
            raise e
    
    
if __name__ == '__main__':
    try :
        logger.info(">>>>>Stage {} started".format(STAGE_NAME))
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(">>>> stage {} completed".format(STAGE_NAME))
    except Exception as e:
        raise e
        