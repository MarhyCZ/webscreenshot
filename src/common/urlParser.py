import os
import json
from pprint import pprint
from typing import Dict, List


CONFIG_PATH = os.path.abspath(os.path.dirname(__file__)) + '/config'


def load_urls() -> Dict[str, List[str]]:
    urlspath = f'{CONFIG_PATH}/urlstocheck.json'
    urls = []
    if os.path.exists(urlspath):
        file = open(urlspath, 'r')
        urls = json.loads(file.read())
        pprint(urls)
    return urls
