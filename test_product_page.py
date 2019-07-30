from pages.login_page import LoginPage
from pages.product_page import ProductPage
import time
import pytest

link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
product_link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_cart(browser, link):
    prod_page = ProductPage(browser, link)
    prod_page.open()
    prod_page.add_product_to_cart()
    prod_page.solve_quiz_and_get_code()
    prod_page.should_be_same_product_price_and_title()


def test_guest_cant_see_success_message(browser):
    prod_page = ProductPage(browser, link)
    prod_page.open()
    prod_page.should_not_be_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    prod_page = ProductPage(browser, product_link)
    prod_page.open()
    prod_page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    prod_page = ProductPage(browser, product_link)
    lpage = LoginPage(browser, product_link)
    prod_page.open()                      
    prod_page.go_to_login_page()       
    lpage.should_be_login_page()
