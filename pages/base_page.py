import logging
from typing import List

from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver):
        self._driver = driver
        self._action = ActionChains(self._driver)

    def open_url(self, url: str):
        logging.debug(f"Launching: {url}")
        self._driver.get(url)

    @property
    def current_url(self):
        return self._driver.current_url

    @property
    def title(self):
        return self._driver.title

    def _wait_until_visible(self, locator: tuple, timeout: int = 30) -> WebElement:
        element = WebDriverWait(self._driver, timeout).until(visibility_of_element_located(locator))
        return element

    def _find_elements(self, locator: tuple) -> List[WebElement]:
        return self._driver.find_elements(*locator)

    def _clear(self, locator: tuple, timeout=30):
        element = self._wait_until_visible(locator, timeout)
        element.clear()

    def _type(self, locator: tuple, text: str, timeout=30):
        element = self._wait_until_visible(locator, timeout)
        element.clear()
        self._action.move_to_element(element).send_keys_to_element(element, text).perform()

    def _click(self, locator: tuple, timeout=30):
        element = self._wait_until_visible(locator, timeout)
        self._action.move_to_element(element).click(element).perform()

    def is_displayed(self, locator: tuple, timeout: int = 30):
        try:
            return self._wait_until_visible(locator, timeout=timeout)
        except (NoSuchElementException, TimeoutException):
            return False
