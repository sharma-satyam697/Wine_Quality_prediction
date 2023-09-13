from src.mlproject.entity.config_entity import DataIngestionConfig
from urllib import request
from src.mlproject import logger
import zipfile
import os
from src.mlproject.utils.common import get_size
from pathlib import Path


class DataIngestion:
    def __init__(self, config : DataIngestionConfig):
        self.config = config
        
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename , headers = request.urlretrieve(
                url = self.config.source_URl,
                filename = self.config.local_data_file
            )
            logger.info("{} download ! with following info {}:".format(filename,headers))
        else:
            logger.info("file already exists of size : {}".format(get_size(Path(self.config.local_data_file))))
            
    
    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            
            zip_ref.extractall(unzip_path)
            