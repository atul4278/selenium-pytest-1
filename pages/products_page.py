import logging

from assertpy import assert_that
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProductsPage(BasePage):
    __inventory_item_container = (By.CSS_SELECTOR, 'div.inventory_item')
    __inventory_item_name = (By.CSS_SELECTOR, 'div.inventory_item_name')
    __add_to_cart_button = (By.CSS_SELECTOR, 'button.btn_primary')
    __cart_item_count = (By.CSS_SELECTOR, 'span.shopping_cart_badge')
    __remove_button = (By.CSS_SELECTOR, 'button.btn_secondary')

    def __init__(self, driver):
        super().__init__(driver)
        self.wait_until_page_load()

    def wait_until_page_load(self):
        self._wait_until_visible(self.__inventory_item_container)

    def get_all_product_names(self):
        products = [product.text for product in self._find_elements(self.__inventory_item_name)]
        logging.info(f"Products: {products}")
        return

    def add_item_to_cart(self, product_name):
        logging.info(f"Add '{product_name}' item to cart")
        product_containers = self._find_elements(self.__inventory_item_container)
        for product in product_containers:
            inventory_name = product.find_element(*self.__inventory_item_name).text
            if inventory_name == product_name:
                product.find_element(*self.__add_to_cart_button).click()
                logging.info("Clicked on 'Add to cart' for item.")
                break
        else:
            raise AssertionError(f"Product NOT found with name: {product_name}")

    def remove_item_from_cart(self, product_name):
        logging.info(f"Remove '{product_name}' item from cart")
        product_containers = self._find_elements(self.__inventory_item_container)
        for product in product_containers:
            inventory_name = product.find_element(*self.__inventory_item_name).text
            if inventory_name == product_name:
                product.find_element(*self.__remove_button).click()
                logging.info("Clicked on 'Remove' button for item.")
                break
        else:
            raise AssertionError(f"Product NOT found with name: {product_name}")

    def get_count_of_items_in_cart(self):
        count = int(self._wait_until_visible(self.__cart_item_count).text)
        logging.info(f"Items in the cart: {count}")
        return count

    def verify_cart_count(self, items_in_cart):
        logging.info("Verify cart count is as expected")
        assert_that(self.get_count_of_items_in_cart()).is_equal_to(items_in_cart)

    def verify_remove_button_is_displayed(self, is_displayed: bool):
        logging.info("Verify 'Remove' button is displayed.")
        if is_displayed:
            assert_that(self.is_displayed(self.__remove_button)).is_true()
        else:
            assert_that(self.is_displayed(self.__remove_button)).is_false()

    def verify_cart_count_is_displayed(self, is_displayed: bool):
        logging.info("Verify cart count badge is displayed.")
        if is_displayed:
            assert_that(self.is_displayed(self.__cart_item_count)).is_true()
        else:
            assert_that(self.is_displayed(self.__cart_item_count)).is_false()