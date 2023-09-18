from src.mlproject.config.configuration import ConfigurationManager
from src.mlproject.components.model_training import ModelTrainer
from src.mlproject import logger



STAGE_NAME = 'Model Training'

class ModelTrainingPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        try: 
            config = ConfigurationManager()
            model_trainer_config = config.get_model_trainer_config()
            model_trainer = ModelTrainer(config=model_trainer_config)
            model_trainer.train()
        except Exception as e:
            raise e


if __name__ == '__main__':
    try :
        logger.info(">>>>>Stage {} started".format(STAGE_NAME))
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(">>>> stage {} completed".format(STAGE_NAME))
    except Exception as e:
        raise e







