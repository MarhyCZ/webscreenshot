from datetime import date, datetime
from pprint import pprint
import time
import pytz
import browser
from common.config import SCREENSHOT_INTERVAL
from common.types import Attachment, BrowserStorage
import exporters.gdrive as gdrive
import common.urlParser as urlParser
import exporters.csv as csv
import exporters.postmark as postmark
from selenium import webdriver


def main():
    start_time = time.time()
    while True:
        # process_screenshot(driver)
        process_storage()
        time.sleep(SCREENSHOT_INTERVAL - (time.time() - start_time) %
                   SCREENSHOT_INTERVAL)


def process_storage():
    url_groups = urlParser.load_urls()
    storage_groups: list[BrowserStorage] = []
    for group_name, urls in url_groups.items():
        storage = browser.export_storage_urls(urls)
        storage.group_name = group_name
        storage_groups.append(storage)

    current_date = date.today().strftime("%d-%m-%Y")
    attachments: list[Attachment] = []
    for storage in storage_groups:
        csv_cookies = csv.generate_csv_cookies(storage.cookies)
        csv_storage = csv.generate_csv_local_storage(storage.local_storage)
        attachments.append(Attachment(
            f"{storage.group_name}_cookies_{current_date}.csv", 'text/csv', csv_cookies))
        attachments.append(Attachment(
            f"{storage.group_name}_local_storage_{current_date}.csv", 'text/csv', csv_storage))
    postmark.send_mail(attachments)


def process_screenshot(driver: webdriver.Chrome):
    screenshot = browser.create_screenshot(driver)

    current_time = datetime.now(tz=pytz.timezone(
        "Europe/Prague")).strftime("%Y-%m-%d %H:%M:%S")
    browser_version = driver.capabilities['browserVersion']
    filename = f"{current_time} Chrome_{browser_version}.png"

    gdrive.upload_basic(filename, screenshot)


if __name__ == "__main__":
    main()
