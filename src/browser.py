import os
from pprint import pprint
from typing import List
from selenium import webdriver
from selenium.webdriver.common.by import By
from common.config import PAGE_TO_SCREENSHOT, WEBDRIVER_URL

from common.types import BrowserStorage


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


def export_storage_urls(urls: List[str]) -> BrowserStorage:
    driver = setup_browser()
    storage = BrowserStorage()
    for url in urls:
        print(url)
        driver.get(url)
        storage.cookies.extend(driver.get_cookies())
        storage.local_storage.extend(driver.execute_script(
            "var ls = window.localStorage, items = []; "
            "for (var i = 0, k; i < ls.length; ++i) "
            "items.push({'name': k = ls.key(i), 'value': ls.getItem(k)});"
            "return items; "))
        # Only unique data
        storage.cookies = [dict(s) for s in set(
            frozenset(d.items()) for d in storage.cookies)]
        storage.local_storage = [dict(s) for s in set(
            frozenset(d.items()) for d in storage.local_storage)]
    driver.quit()
    return storage


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
