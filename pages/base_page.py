import logging

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver: WebDriver):
        self._driver = driver
        self._action = ActionChains(self._driver)

    def go_to(self, url: str):
        logging.debug(f"Launching: {url}")
        self._driver.get(url)

    def wait_until_visible(self, locator: tuple, timeout=30) -> WebElement:
        element = WebDriverWait(self._driver, timeout).until(visibility_of_element_located(locator))
        return element

    def clear(self, locator: tuple, timeout=30):
        element = self.wait_until_visible(locator, timeout)
        element.clear()

    def type(self, locator: tuple, text: str, timeout=30):
        element = self.wait_until_visible(locator, timeout)
        element.clear()
        self._action.move_to_element(element).send_keys_to_element(element, text).perform()

    def click(self, locator: tuple, timeout=30):
        element = self.wait_until_visible(locator, timeout)
        self._action.move_to_element(element).click(element).perform()
