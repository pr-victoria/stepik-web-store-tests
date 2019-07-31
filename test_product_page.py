from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
import time
import pytest
import faker

link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
product_link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"


@pytest.mark.registered_user
class TestUserAddToCartFromProductPage(object):
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        f = faker.Faker()
        reg_link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        login_page = LoginPage(browser, reg_link)
        login_page.open()
        login_page.register_new_user(f.email(), "12345pwd!")
        login_page.should_be_authorized_user()

    @pytest.mark.need_review
    @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                      pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                                   marks=pytest.mark.xfail(reason="bug")),
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
    def test_user_can_add_product_to_cart(self, browser, link):
        prod_page = ProductPage(browser, link)
        prod_page.open()
        prod_page.add_product_to_cart()
        prod_page.solve_quiz_and_get_code()
        prod_page.should_be_same_product_price_and_title()

    def test_user_cant_see_success_message(self, browser):
        prod_page = ProductPage(browser, link)
        prod_page.open()
        prod_page.should_not_be_success_message()


@pytest.mark.need_review
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                               marks=pytest.mark.xfail(reason="bug")),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_cart(browser, link):
    prod_page = ProductPage(browser, link)
    prod_page.open()
    prod_page.add_product_to_cart()
    prod_page.solve_quiz_and_get_code()
    prod_page.should_be_same_product_price_and_title()


def test_guest_should_see_login_link_on_product_page(browser):
    prod_page = ProductPage(browser, product_link)
    prod_page.open()
    prod_page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    prod_page = ProductPage(browser, product_link)
    login_page = LoginPage(browser, product_link)
    prod_page.open()
    prod_page.go_to_login_page()
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    prod_page = ProductPage(browser, product_link)
    cart_page = CartPage(browser, product_link)
    prod_page.open()
    prod_page.go_to_cart_page()
    cart_page.should_be_empty_cart()
