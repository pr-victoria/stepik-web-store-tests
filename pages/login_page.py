from pages.base_page import BasePage
from pages.locators import LoginPageLocators
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        email_field = self.browser.wait.until(EC.visibility_of_element_located(
            (LoginPageLocators.REGISTRATION_EMAIL)))
        email_field.send_keys(email)
        password_field = self.browser.wait.until(EC.visibility_of_element_located(
            (LoginPageLocators.REGISTRATION_PWD)))
        password_field.send_keys(password)
        conf_password_field = self.browser.wait.until(EC.visibility_of_element_located(
            (LoginPageLocators.REGISTRATION_CONFIRM_PWD)))
        conf_password_field.send_keys(password)
        submit = self.browser.wait.until(EC.element_to_be_clickable(
            (LoginPageLocators.REGISTER_BTN)))
        submit.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "'login' substring is not in {}".format(
            self.browser.current_url)

    def should_be_login_form(self):
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_FORM), "Registration form is not presented"
