from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")


class LoginPageLocators(object):
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators(object):
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.TAG_NAME, "h1")
    MESSAGE_PRICE = (By.CSS_SELECTOR, ".alert-info strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
