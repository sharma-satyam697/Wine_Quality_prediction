import os
from box.exceptions import  BoxValueError
import yaml
from src.mlproject import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import  Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml : Path) -> ConfigBox:
    """
    reads yaml file and returns
    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError : if yaml file is empty
        e : empty file
    Retuns:
        ConfigBox : configBox type
    :param path_to_yaml:
    :return:
    """

    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info("yaml file : {} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError('yaml file is empty')
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories : list, verbose=True):
    """
    creating a list of directories

    :param path_to_directories: list of path of directories
    :param verbose: Wether to display verbose output
    :return: If verbose =True , get message in log else leave it
    """
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info('Created directory : {}'.format(path))

@ensure_annotations
def save_json(path : Path, data : dict):
    """

    :param path: path to json file
    :param data: data to be saved in json file
    :return:
    """
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)

    logger.info('Json file saved at : {}'.format(path))


@ensure_annotations
def load_json(path : Path) -> ConfigBox:
    """

    :param path: path to json file
    :return: Configbox : data as class attributes instead of dic
    """

    with open(path) as f:
        content = json.load(f)
    logger.info("Json file loaded successfully from : {}".format(path))
    return content

@ensure_annotations
def save_bin(data : Any, path : Path):
    """

    :param data: data to be serialized into binary
    :param path: path to binary file
    :return:
    """
    data = joblib.dump(value=data , filename=path)
    logger.info("binary file saved at : {}".format(path))

@ensure_annotations
def load_bin(path : Path) -> Any:
    """
    load binary data
    :param path: path to binary file
    :return:
    """
    data = joblib.load(path)
    logger.info("Data loaded successfully from : {}".format(path))
    return data

@ensure_annotations
def get_size(path : Path) -> Any:
    """
    get size in kb
    :param path: path to the file
    :return: size in kb (str)
    """
    size_in_kb = (os.path.getsize(path))
    return "{}kb".format(size_in_kb)

