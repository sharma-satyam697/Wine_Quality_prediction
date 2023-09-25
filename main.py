
from src.mlproject.pipeline.stage_01_data_ingestion import  DataIngestionTrainingPipeline
from src.mlproject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from src.mlproject.pipeline.stage_03_datatransformation import DataTransformationTrainingPipeline
from src.mlproject.pipeline.stage_04_model_training import ModelTrainingPipeline
from src.mlproject.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline
from src.mlproject import logger

STAGE_NAME= 'Data Ingestion stage'
try:
    logger.info(">>>>>Stage {} started".format(STAGE_NAME))
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(">>>> stage {} completed".format(STAGE_NAME))    
    
except Exception as e:    
    logger.exception(e)
    raise e


# Data Validation process
STAGE_NAME= 'Data Validation stage'

try:
    logger.info(">>>>>Stage {} started".format(STAGE_NAME))
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(">>>> stage {} completed".format(STAGE_NAME))    
    
except Exception as e:    
    logger.exception(e)
    raise e

# Data Transformation process
STAGE_NAME = 'Data Transformation stage'
try :
    logger.info(">>>>>Stage {} started".format(STAGE_NAME))
    obj = DataTransformationTrainingPipeline()
    obj.main()
    logger.info(">>>> stage {} completed".format(STAGE_NAME))
except Exception as e:
        raise e

# Model training
STAGE_NAME = 'Model Trainer stage'
try :
    logger.info(">>>>>Stage {} started".format(STAGE_NAME))
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(">>>> stage {} completed".format(STAGE_NAME))
except Exception as e:
    raise e

# Model Evaluation
STAGE_NAME = 'Model Evaluation'


try :
    logger.info(">>>>>Stage {} started".format(STAGE_NAME))
    obj = ModelEvaluationTrainingPipeline()
    obj.main()
    logger.info(">>>> stage {} completed".format(STAGE_NAME))
except Exception as e:
    raise e

