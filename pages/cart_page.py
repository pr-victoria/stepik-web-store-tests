from pages.locators import CartPageLocators
from pages.base_page import BasePage


class CartPage(BasePage): 
    def should_not_be_products(self):
        assert self.is_not_element_present(*CartPageLocators.CART_ITEM), \
            "Product is presented, but should not be"

    def should_be_empty_text(self):
        assert self.is_element_present(*CartPageLocators.EMPTY_TEXT), \
            "Empty cart text is not presented"

    def should_be_empty_cart(self):
        self.should_not_be_products()
        self.should_be_empty_text()
