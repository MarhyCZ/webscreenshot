from datetime import datetime
import os
from pprint import pprint
import time
import pytz
import browser
import gdrive
import urlParser
from selenium import webdriver

SCREENSHOT_INTERVAL = int(os.environ['SCREENSHOT_INTERVAL'])


def main():
    start_time = time.time()
    while True:
        driver = browser.setup_browser()
        # process_screenshot(driver)
        process_storage(driver)
        driver.quit()
        time.sleep(SCREENSHOT_INTERVAL - (time.time() - start_time) %
                   SCREENSHOT_INTERVAL)


def process_storage(driver: webdriver.Chrome):
    url_groups = urlParser.load_urls()
    for group_name, urls in url_groups.items():
        data = browser.export_storage_urls(driver, urls)
        cookies = data['cookies']
        local_storage = data['local_storage']
        pprint(local_storage)


def process_screenshot(driver: webdriver.Chrome):
    screenshot = browser.create_screenshot(driver)

    current_time = datetime.now(tz=pytz.timezone(
        "Europe/Prague")).strftime("%Y-%m-%d %H:%M:%S")
    browser_version = driver.capabilities['browserVersion']
    filename = f"{current_time} Chrome_{browser_version}.png"

    gdrive.upload_basic(filename, screenshot)


if __name__ == "__main__":
    main()
