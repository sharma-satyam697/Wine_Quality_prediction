from sklearn.model_selection import train_test_split
from src.mlproject.config.configuration import DataTransformationConfig
from src.mlproject import logger
import os
import pandas as pd




class DataTransformation:
    def __init__(self, config = DataTransformationConfig):
        self.config = config
        
    def train_test_splitting(self):
        ## Read data from csv file
        data = pd.read_csv(self.config.data_path,sep=';')
        ## train and test split
        train, test  = train_test_split(data)
        logger.info('Splitted data into train and test sets')
        
        train.to_csv(os.path.join(self.config.root_dir, 'train.csv'),index=False)
        test.to_csv(os.path.join(self.config.root_dir, 'test.csv'),index=False)
        
        logger.info(train.shape)
        logger.info(test.shape)
        
        
    # can create methods for data transorming..like cleaning etc.
    
    
  