from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.locators import ProductPageLocators
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class ProductPage(BasePage):
    def add_product_to_cart(self):
        btn = self.browser.wait.until(EC.element_to_be_clickable(
            (ProductPageLocators.ADD_TO_BASKET_BTN)))
        btn.click()

    def should_be_product_title_in_message(self):
        product_title = self.browser.wait.until(
            EC.visibility_of_element_located((ProductPageLocators.PRODUCT_NAME))).text
        print(product_title)
        message_title = self.browser.wait.until(
            EC.visibility_of_element_located((ProductPageLocators.PRODUCT_NAME))).text
        assert self.is_element_present(*(By.XPATH, '//*[contains(@class, "alert-success")]//strong[text() = "{}"]'.format(
            product_title))), "Product title is different or not found"

    def should_be_product_price_in_message(self):
        product_price = self.browser.wait.until(
            EC.visibility_of_element_located(ProductPageLocators.PRODUCT_PRICE)).text
        message_price = self.browser.wait.until(
            EC.visibility_of_element_located(ProductPageLocators.MESSAGE_PRICE)).text
        assert product_price == message_price

    def should_be_same_product_price_and_title(self):
        self.should_be_product_title_in_message()
        self.should_be_product_price_in_message()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is present, but should not be"
