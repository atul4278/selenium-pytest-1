from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProductsPage(BasePage):
    __inventory_item_container = (By.CSS_SELECTOR, 'div.inventory_item')

    def __init__(self, driver):
        super().__init__(driver)
        self.wait_until_page_load()

    def wait_until_page_load(self):
        self.wait_until_visible(self.__inventory_item_container)
