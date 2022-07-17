from selenium import webdriver
from selenium.webdriver.common.by import By

PAGE_TO_SCREENSHOT = 'https://www.o2.cz/'


def setup_browser() -> webdriver.Chrome:
    options = webdriver.ChromeOptions()
    # options.add_argument('--ignore-ssl-errors=yes')
    # options.add_argument('--ignore-certificate-errors')

    driver = None
    while driver is None:
        try:
            # Try connecting to other container until its up/running
            driver = webdriver.Remote(
                command_executor='http://selenium:4444/wd/hub',
                options=options
            )
        except:
            pass
    return driver


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
