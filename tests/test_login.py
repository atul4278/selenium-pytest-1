import pytest

from pages.login_page import LoginPage
from assertpy import assert_that


@pytest.mark.login
class TestLogin:
    def test_valid_login(self, driver, config):
        loginPage = LoginPage(driver)
        loginPage.open_url(config.get('url'))
        _ = loginPage.execute_login(config.get("standard_user"), config.get("password"))

    def test_invalid_username(self, driver, config):
        loginPage = LoginPage(driver)
        loginPage.open_url(config.get('url'))
        loginPage.enter_username('fake_username')
        loginPage.enter_password(config.get("standard_user"))
        loginPage.click_login()
        error = loginPage.get_error_message_text()
        assert_that(error).contains("Username and password do not match any user in this service")

    def test_invalid_password(self, driver, config):
        loginPage = LoginPage(driver)
        loginPage.open_url(config.get('url'))
        loginPage.enter_username(config.get("standard_user"))
        loginPage.enter_password("fake_password")
        loginPage.click_login()
        error = loginPage.get_error_message_text()
        assert_that(error).contains("Username and password do not match any user in this service")

    def test_locked_user(self, driver, config):
        loginPage = LoginPage(driver)
        loginPage.open_url(config.get('url'))
        loginPage.enter_username("locked_out_user")
        loginPage.enter_password(config.get("password"))
        loginPage.click_login()
        error = loginPage.get_error_message_text()
        assert_that(error).contains("Sorry, this user has been locked out.")
