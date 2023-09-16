from src.mlproject.config.configuration import ConfigurationManager
from src.mlproject.components.data_validation import DataValidation
from src.mlproject import logger

STAGE_NAME = 'Data Validation stage'

class DataValidationTrainingPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        try: 
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config()
            data_validation = DataValidation(config=data_validation_config)
            data_validation.validate_all_columns()
        except Exception as e:
            raise e
        

if __name__ == "__main__ :":
    try : 
        logger.info(">>>>>Stage {} started".format(STAGE_NAME))
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(">>>> stage {} completed".format(STAGE_NAME))        
        
    except Exception as e:
        logger.exception(e)
        raise e