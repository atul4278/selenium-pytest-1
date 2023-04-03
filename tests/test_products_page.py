import time

import pytest
from assertpy import assert_that

from pages.login_page import LoginPage
from pages.products_page import ProductsPage


@pytest.mark.inventory
class TestProductsPage:
    @pytest.fixture(scope='class', autouse=True)
    def setup(self, driver, config):
        driver.get(config['url'])
        login_page = LoginPage(driver)
        login_page.execute_login(config['standard_user'], config['password'])

    def test_product_names_are_displayed(self, driver):
        products_page = ProductsPage(driver)
        assert_that(products_page.get_all_product_names()).is_length(6)

    def test_item_can_be_added_to_cart(self, driver):
        products_page = ProductsPage(driver)
        products_page.add_item_to_cart("Sauce Labs Fleece Jacket")
        time.sleep(1)
        try:
            products_page.verify_cart_count_is_displayed(is_displayed=True)
            products_page.verify_cart_count(1)
            products_page.verify_remove_button_is_displayed(is_displayed=True)
        finally:
            products_page.remove_item_from_cart("Sauce Labs Fleece Jacket")

    def test_item_can_be_removed_from_cart(self, driver):
        products_page = ProductsPage(driver)
        products_page.add_item_to_cart("Sauce Labs Backpack")
        time.sleep(1)
        products_page.verify_cart_count(1)
        products_page.remove_item_from_cart("Sauce Labs Backpack")
        time.sleep(1)
        products_page.verify_cart_count_is_displayed(is_displayed=False)
