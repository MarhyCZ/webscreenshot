import os
import json
from typing import Dict, List

from common.config import CONFIG_PATH


def load_urls() -> Dict[str, List[str]]:
    urlspath = f'{CONFIG_PATH}/urlstocheck.json'
    urls = []
    if os.path.exists(urlspath):
        file = open(urlspath, 'r')
        urls = json.loads(file.read())
    return urls
