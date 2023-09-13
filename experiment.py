from box import ConfigBox

from src.mlproject import logger
import json
from pathlib import  Path
data1 = {
    'name ' : ['satyam','mukesh','paramchand','suresh','pappu'],
    'ages' : [34, 54,356,23,5,34]
}

def dump_json(path : Path, data : dict):
    with open(path , 'w') as f:
        json.dump(data,f, indent=10)
    logger.info("Content has been dumped in json file , path is {}".format(path))


path  = Path('templates/temp.json')

def load_json(path : Path) -> ConfigBox:
    """

    :param path: path to json file
    :return: Configbox : data as class attributes instead of dic
    """

    with open(path) as f:
        content = json.load(f)
    logger.info('infor',content)
    logger.info("Json file loaded successfully from : {}".format(path))
    return content

load_json(path)
import  os
def get_size(path : Path) -> str:
    """
    get size in kb
    :param path: path to the file
    :return: size in kb (str)
    """
    size_in_kb = (os.path.getsize(path))
    return "{}kb".format(size_in_kb)

print(get_size(Path('template.py')))