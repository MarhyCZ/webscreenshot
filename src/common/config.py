import os
import sys

SCREENSHOT_INTERVAL = int(os.environ['SCREENSHOT_INTERVAL'])
ROOT_FOLDER_ID = os.environ['ROOT_FOLDER_ID']
PAGE_TO_SCREENSHOT = os.environ['PAGE_TO_SCREENSHOT']

PROJECT_PATH = os.path.abspath(
    os.path.dirname(sys.modules['__main__'].__file__))
CONFIG_PATH = PROJECT_PATH + '/config'

WEBDRIVER_URL = 'http://localhost:4444/wd/hub'
