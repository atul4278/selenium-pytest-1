from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


def get_driver_object(browser) -> WebDriver:
    driver = None
    if browser.lower() == 'chrome':
        from selenium.webdriver.chrome.service import Service
        from webdriver_manager.chrome import ChromeDriverManager
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    return driver
