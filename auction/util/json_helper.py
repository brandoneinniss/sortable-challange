import os
import json


def get_json_file_content(path):
    """Load json data from file and return data"""
    if not isinstance(path, str) or not os.path.exists(path):
        raise TypeError('invalid path given')
    try:
        with open(path) as data_file:
            data = json.load(data_file)
        return data
    except Exception as e:
        raise SyntaxError(path + '-' + str(e))
