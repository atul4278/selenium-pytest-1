from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    __username_field = (By.CSS_SELECTOR, 'input#user-name')
    __password_field = (By.CSS_SELECTOR, 'input#password')
    __login_button = (By.CSS_SELECTOR, 'input#login-button')
    __error_message = (By.CSS_SELECTOR, 'h3')

    def __init__(self, driver):
        super().__init__(driver)

    def enter_username(self, username):
        self._type(self.__username_field, username)

    def enter_password(self, password):
        self._type(self.__password_field, password)

    def click_login(self):
        self._click(self.__login_button)

    def execute_login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        from pages.products_page import ProductsPage
        return ProductsPage(self._driver)

    def get_error_message_text(self):
        return self._wait_until_visible(self.__error_message).text
