from datetime import datetime
import time
import pytz
import browser
import gdrive
from selenium import webdriver


def main():
    driver = browser.setup_browser()
    start_time = time.time()
    while True:
        process_screenshot(driver)
        time.sleep(21600 - (time.time() - start_time) % 21600.00)


def process_screenshot(driver: webdriver.Chrome):
    screenshot = browser.create_screenshot(driver)

    current_time = datetime.now(tz=pytz.timezone(
        "Europe/Prague")).strftime("%Y-%m-%d %H:%M:%S")
    browser_version = driver.capabilities['browserVersion']
    filename = f"{current_time} Chrome_{browser_version}.png"

    gdrive.upload_basic(filename, screenshot)


if __name__ == "__main__":
    main()
