from src.mlproject.config.configuration import ModelEvaluationConfig
import json
import pandas as pd
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import joblib


class ModelEvaluation:
    def __init__(self,config : ModelEvaluationConfig):
        self.config = config
            
    def eval_metrics(self, actual,pred):
        r2 = r2_score(actual,pred)
        mse = mean_squared_error(actual,pred)
        mae = mean_absolute_error(actual,pred)
        return r2,mae,mse
    
    def log_into_mlflow(self):
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)
        
        x_test = test_data.drop(self.config.target_column,axis=1)
        y_test = test_data[[self.config.target_column]]
        
        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme
        
        with mlflow.start_run():
            predicted_qualities = model.predict(x_test)
            (r2,mae,mse) = self.eval_metrics(y_test,predicted_qualities)
            
            # saving metrics as local
            scores = {'mse': mse , 'mae' : mae, 'r2' : r2}
            with open(self.config.metric_file_name, 'w') as json_file:
                
                json.dump(scores,json_file)
                
            mlflow.log_params(self.config.all_params)
            mlflow.log_metric('r2',r2)
            mlflow.log_metric('mae', mae)
            mlflow.log_metric('mse', mse)
            
            if tracking_url_type_store != 'file':
                
                mlflow.sklearn.log_model(model,'model',registered_model_name='ElasticNet')
            else:
                mlflow.sklearn.log_model(model ,'model')
                
            
            
    