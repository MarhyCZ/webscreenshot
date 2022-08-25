import os
from pprint import pprint
from typing import List
from selenium import webdriver
from selenium.webdriver.common.by import By

PAGE_TO_SCREENSHOT = os.environ['PAGE_TO_SCREENSHOT']
WEBDRIVER_URL = 'http://localhost:4444/wd/hub'


def setup_browser() -> webdriver.Chrome:
    options = webdriver.ChromeOptions()
    # options.add_argument('--ignore-ssl-errors=yes')
    # options.add_argument('--ignore-certificate-errors')

    driver = None
    while driver is None:
        try:
            # Try connecting to other container until its up/running
            driver = webdriver.Remote(
                command_executor=WEBDRIVER_URL,
                options=options
            )
        except:
            pass
    return driver


def export_storage_urls(driver: webdriver.Chrome, urls: List[str]):
    cookies = []
    local_storage = []
    for url in urls:
        print(url)
        driver.get(url)
        cookies.append(driver.get_cookies())
        local_storage.append(driver.execute_script(
            "var ls = window.localStorage, items = {}; "
            "for (var i = 0, k; i < ls.length; ++i) "
            "  items[k = ls.key(i)] = ls.getItem(k); "
            "return items; "))
    data = {'cookies': cookies, 'local_storage': local_storage}
    return data


def create_screenshot(driver: webdriver.Chrome) -> bytes:
    driver.get(PAGE_TO_SCREENSHOT)
    # Ref: https://stackoverflow.com/a/52572919/
    driver.set_window_size(1440, 2000)
    required_height = driver.execute_script(
        'return document.body.parentNode.scrollHeight')
    driver.set_window_size(1440, required_height)
    # driver.save_screenshot(path) has scrollbar
    # Without scrollbar:
    screenshot = driver.find_element(By.TAG_NAME, 'body').screenshot_as_png
    return screenshot
