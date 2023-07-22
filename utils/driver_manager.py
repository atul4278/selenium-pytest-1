from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


def get_driver_object(browser: str, headless: bool) -> WebDriver:
    driver = None
    if browser.lower() == 'chrome':
        from selenium.webdriver.chrome.options import Options
        options = Options()
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors=yes')
        options.add_argument('--start-maximized')
        if headless:
            options.add_argument('--headless=new')
        driver = webdriver.Chrome(options=options)
    elif browser.lower() == 'firefox':
        from selenium.webdriver.firefox.options import Options
        options = Options()
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors=yes')
        if headless:
            options.add_argument('--headless')
        driver = webdriver.Firefox(options=options)

    return driver
