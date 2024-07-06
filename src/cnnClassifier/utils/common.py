import os
import yaml
import json
import joblib
import base64

from box.exceptions import BoxValueError
from box import ConfigBox
from pathlib import Path
from typing import Any

from cnnClassifier import logger

def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads a yaml file and returns a ConfigBox object
    Args:
        path_to_yaml (Path): path to yaml file
    Returns:
        ConfigBox: ConfigBox object    
    """
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f'Loaded yaml file from {path_to_yaml}')
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError(f'Error reading yaml file from {path_to_yaml}. File empty?')
    except Exception as e:
        raise e
    
def create_directories(path_to_dir: list, verbose=True):
    """creates directories
    Args:
        path_to_dir (list[str]): list of paths to directories
    """
    for path in path_to_dir:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f'Created directory: {path}')

def save_json(path: Path, data: dict):
    """saves data to a json file
    Args:
        path (Path): path to json file
        data (Any): data to save
    """
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)

    logger.info(f'Saved json file to {path}')

def load_json(path: Path) -> ConfigBox:
    """loads data from a json file
    Args:
        path (Path): path to json file
    Returns:
        ConfigBox: ConfigBox object
    """
    with open(path, 'r') as f:
        data = json.load(f)
    
    logger.info(f'Loaded json file from {path}')
    return ConfigBox(data)

def load_bin(path: Path) -> Any:
    """loads data from a binary file
    Args:
        path (Path): path to binary file
    Returns:
        Any: data
    """
    data = joblib.load(path)
    logger.info(f'Loaded binary file from {path}')
    return data

def get_size(path: Path) -> str:
    """returns the size of a file in KB
    Args:
        path (Path): path to file
    Returns:
        str: size of file string
    """
    size_kb = round(os.path.getsize(path)/1024, 2)
    return f'~ {size_kb} KB'

def decodeImage(imgString, fileName):
    """decodes image string and saves image
    Args:
        imgString (str): image string
        fileName (str): file name
    """
    imgdata = base64.b64decode(imgString)
    with open(fileName, 'wb') as f:
        f.write(imgdata)

def encodeImageIntoBase64(croppedImagePath):
    """encodes image into base64
    Args:
        croppedImagePath (str): path to image
    Returns:
        str: image string
    """
    with open(croppedImagePath, "rb") as img_file:
        return base64.b64encode(img_file.read())