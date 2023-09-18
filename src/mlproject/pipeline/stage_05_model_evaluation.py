from src.mlproject.config.configuration import ConfigurationManager
from src.mlproject.components.model_evaluation import ModelEvaluation
from src.mlproject import logger




STAGE_NAME = 'Model Evaluation'

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        model_evaluation.log_into_mlflow()
        









if __name__ == '__main__':
    try :
        logger.info(">>>>>Stage {} started".format(STAGE_NAME))
        obj = ModelEvaluationTrainingPipeline()
        obj.main()
        logger.info(">>>> stage {} completed".format(STAGE_NAME))
    except Exception as e:
        raise e