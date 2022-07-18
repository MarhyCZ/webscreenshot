from datetime import datetime
import os
import time
import pytz
import browser
import gdrive
from selenium import webdriver

SCREENSHOT_INTERVAL = int(os.environ['SCREENSHOT_INTERVAL'])


def main():
    start_time = time.time()
    while True:
        driver = browser.setup_browser()
        process_screenshot(driver)
        time.sleep(SCREENSHOT_INTERVAL - (time.time() - start_time) %
                   SCREENSHOT_INTERVAL)


def process_screenshot(driver: webdriver.Chrome):
    screenshot = browser.create_screenshot(driver)

    current_time = datetime.now(tz=pytz.timezone(
        "Europe/Prague")).strftime("%Y-%m-%d %H:%M:%S")
    browser_version = driver.capabilities['browserVersion']
    filename = f"{current_time} Chrome_{browser_version}.png"

    gdrive.upload_basic(filename, screenshot)


if __name__ == "__main__":
    main()
